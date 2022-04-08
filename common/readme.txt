--------------------------------- Xpath ----------------------------------------

Prepare web for test: google.com and search with 'Selenium'

1. Element by contains
=> Find element by speicific property contains something
=> //{element}[contains(property, {contains_text})]
=> //h4/a[contains(text(),'SAP M')]
=> Contains with multiple condition
=> //a[contains(@class, 'l') and contains(text(), 'Documentation') ]

2. Sibling element 
=> Find the element next on the specific element 
=> This is same level between sibling elements
=> It will find the sibling only on the parent of the specific element. It isn't find on another element
=> current_x_path/following-sibling::{element_type}
=> //tr[contains(@class, 'mslg dmenKe')]/following-sibling::tr

Nodes that have the same parent.
In the following example; the title, author, year, and price elements are all siblings:
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

3. Following element
=> Find the folliwng element from the current element. 
=> Can be element that existing in the another parent class also
=> //tr[contains(@class, 'mslg dmenKe')]/following::tr

4. Parent element
=> Find the parent element from the exisiting element
=> Can be only one step from the existing element
=> This is different level between exisiting element and parent element
=> //div[contains(@class, 'BYM4Nd')]/parent::div
=> Thiis example the div('BYM4Nd') is a child element of another div 

Each element and attribute has one parent.
In the following example; the book element is the parent of the title, author, year, and price:
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

5. Ancestor element
=> Find the parent/grand parent element from the exisitng element
=> Can be multiple step from the existing element
=> This is different level between exisiting element and parent/grand parent element
=> //div[contains(@class, 'BYM4Nd')]/ancestor::div[contains(@class, 'g')]
=> This example the div('BYM4Nd') is under the element div('g') 

A node's parent, parent's parent, etc.
In the following example; the ancestors of the title element are the book element and the bookstore element:

<bookstore>
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
</bookstore>

6. Preceding element
=> Find the element before current element 
=> The preceding element and current element are the same level
=> Can be preceding element that exist in the another parent element
=> //tr[contains(@class, 'mslg c9EJob')]//preceding::tr

7. Descendant element
=> Find the child element that follow by specific parent element 
=> The descendant element and current element are different level
=> The descendant element is exist  specific element
=> //tr[contains(@class, 'mslg c9EJob')]//descendant::div

A node's children, children's children, etc.
In the following example; descendants of the bookstore element are the book, title, author, year, and price elements:

<bookstore>
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
</bookstore>

8. Element by starts-with
=> Find the element by property contains property strat with some text
=> Find the element whose attribute dynamically changes on refresh or other 
   operations like click, submit, etc.
=> //div[starts-with(@class, 'BYM4Nd')]

------------------------------ Selecting Nodes ---------------------------------
nodename        Selects all nodes with the name "nodename"
/               Selects from the root node
//              Selects nodes in the document from the current node that match the selection no matter where they are
.               Selects the current node
..              Selects the parent of the current node
@               Selects attributes


-------------------------------- Predicates ------------------------------------
/bookstore/book[1]                  Selects the first book element that is the child of the bookstore element
/bookstore/book[last()]             Selects the last book element that is the child of the bookstore element
/bookstore/book[last()-1]           Selects the last but one book element that is the child of the bookstore element
/bookstore/book[position()<3]       Selects the first two book elements that are children of the bookstore element
//title[@lang]                      Selects all the title elements that have an attribute named lang
//title[@lang='en']                 Selects all the title elements that have a "lang" attribute with a value of "en"
/bookstore/book[price>35.00]        Selects all the book elements of the bookstore element that have a price element with a value greater than 35.00
/bookstore/book[price>35.00]/title  Selects all the title elements of the book elements of the bookstore element that have a price element with a value greater than 35.00

----------------------------- Selecting Unknown Nodes --------------------------
/bookstore/*    Selects all the child element nodes of the bookstore element
//*             Selects all elements in the document
//title[@*]     Selects all title elements which have at least one attribute of any kind


----------------------------- Selecting Several Paths --------------------------
//book/title | //book/price         Selects all the title AND price elements of all book elements
//title | //price                   Selects all the title AND price elements in the document
/bookstore/book/title | //price     Selects all the title elements of the book element of the bookstore element AND all the price elements in the document

----------------------------------- XPath Axes ---------------------------------

AxisName    	    Result
ancestor	        Selects all ancestors (parent, grandparent, etc.) of the current node
ancestor-or-self	Selects all ancestors (parent, grandparent, etc.) of the current node and the current node itself
attribute	        Selects all attributes of the current node
child	            Selects all children of the current node
descendant	        Selects all descendants (children, grandchildren, etc.) of the current node
descendant-or-self	Selects all descendants (children, grandchildren, etc.) of the current node and the current node itself
following	        Selects everything in the document after the closing tag of the current node
following-sibling	Selects all siblings after the current node
namespace	        Selects all namespace nodes of the current node
parent	            Selects the parent of the current node
preceding	        Selects all nodes that appear before the current node in the document, except ancestors, attribute nodes and namespace nodes
preceding-sibling	Selects all siblings before the current node
self	            Selects the current node

Example	                Result
child::book	            Selects all book nodes that are children of the current node
attribute::lang	        Selects the lang attribute of the current node
child::*	            Selects all element children of the current node
attribute::*	        Selects all attributes of the current node
child::text()	        Selects all text node children of the current node
child::node()	        Selects all children of the current node
descendant::book	    Selects all book descendants of the current node
ancestor::book	        Selects all book ancestors of the current node
ancestor-or-self::book	Selects all book ancestors of the current node - and the current as well if it is a book node
child::*/child::price	Selects all price grandchildren of the current node


------------------------------ XPath Operators ---------------------------------
Operator	            Description	                Example
|	                Computes two node-sets	    //book | //cd
+	                Addition	                6 + 4
-	                Subtraction	                6 - 4
*	                Multiplication	            6 * 4
div	                Division	                8 div 4
=	                Equal	                    price=9.80
!=	                Not equal	                price!=9.80
<	                Less than	                price<9.80
<=	                Less than or equal to	    price<=9.80
>	                Greater than	            price>9.80
>=	                Greater than or equal to	price>=9.80
or	                or	                        price=9.80 or price=9.70
and	                and	                        price>9.00 and price<9.90
mod	                Modulus                 	5 mod 2