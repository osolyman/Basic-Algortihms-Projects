we are implementing a http Router handler using a Trie Algorithm.

RouteTrieNode.insert:
                    Time Complexity: O(1)
                    Space Complexity: O(1)

RouteTrie.insert:
                    Time Complexity: O(n), where n is the number of parts in path
                    Space Complexity: O(n), where n is the number of nodes in the path

RouteTrie.find:
                    Time Complexity: O(n), where n is the number of parts in path
                    Space Complexity: O(n), where n is the number of nodes in the path

Router.split_path:
                    Time Complexity: O(n), where n is the number of characters in path
                    Space Complexity: O(n), where n is the number of nodes in the path

overall time complexity is O(n) for insertion and lookup, where n is the number of parts or characters in the path.

The space complexity is O(n), where n is the number of nodes in the trie.