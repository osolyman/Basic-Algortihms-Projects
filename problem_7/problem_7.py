## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None # handler has been added

    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()

## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        parts = path.split("/") # split the paths to parts

        for part in parts: # iterate through each part after split
            if part:
                current_node.insert(part) # inserting that part to the current node
                current_node = current_node.children[part] # moving the current node pointer to the node in children
        current_node.handler = handler # assigning the handler to only the leaf (deepest) node of this path

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        parts = path.split("/")

        for part in parts:
            if part:
                if part not in current_node.children:
                    return None
                current_node = current_node.children[part]
        return current_node.handler

## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie() # the route trie that holds our routes
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if not path or path == "":
            path_parts = [""]
        
        else:
            path_parts = self.split_path(path) # calling the split method
        self.route_trie.insert("/" + "/".join(path_parts), handler) # calling the insert method to add handler for a path
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/":
            return self.root_handler
        
        if not path:
            return
        
        # this case solved from ChatGPT
        if path[-1] == "/":
            path = path[:-1]
        handler = self.route_trie.find(path)

        if handler is None:
            return self.not_found_handler
        return handler
    
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [part for part in path.split("/") if part]
    
## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'

print("----------------------------------------------------------------------")

# Test Case including handler for an empty path
router = Router("root handler", "not found handler")
router.add_handler("", "empty path handler")

print("Added Test Case.")
print(router.lookup("/"))            # should print 'root handler'
print(router.lookup(""))             # should print 'None'
print(router.lookup("/home"))        # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'not found handler'