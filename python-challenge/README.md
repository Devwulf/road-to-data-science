## Challenges

### How to answer?
Usually, after finding the answer, copy the answer and replace the end of the URL address with `{answer}.html`.

### 00
A simple challenge to calculate the value of 2^38.

### 01
This challenge involves a **Caesar cipher**, where each character of the input text is shifted **n** times along the alphabet. This is easily solved by using `str.maketrans()` to create a mapping between the original alphabet and the shifted alphabet, and using that mapping to translate the input text. As the input text suggests, translating the page `.html` file name (which was **map**) gives the answer.

### 02
This challenge involves getting the rarest characters among a very long string of characters. This is as simple as going through each of the character in the string and tracking the instances of each unique character onto a dictionary. Finally, the dictionary is sorted in the ascending direction by the instance count of each character to get the final answer.

### 03
This challenge involves finding, from a very long string of alphabet characters, any substrings of the format **AAAbAAA**, where A's are any uppercase letters, while b is any lowercase letter. This can easily be solved by using Regex to find any substrings of the specified pattern. One Regex string that could be used is:

```
[A-Z]{3}[a-z][A-Z]{3}
```

Since only substrings of the specified pattern counts (e.g., **AAAAbAAA** or **AAAbAAAA** or **AAAAbAAAA** will not count), the pattern to look for can change to **bAAAbAAAb**, which in Regex is:

```
[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]
```

This will give us multiple substrings, where the middle lowercase letters will form a word when put together.

### 04
This challenge involves querying a web server using **"nothing"** values. Querying the server with a **"nothing"** value will lead to a page with another **"nothing"** value written on it. Some pages give texts where user intervention is required to continue, while some pages will be tricky and give two numbers, but only one counts. Regex is used here, and to prevent being tricked and automating as much as possible, this regex is used:

```
[nN]ext nothing is (\d+)
```
The number by itself can be taken by using `match.group(1)`. Following this trail of **"nothing"** values will result in the URL page to go to next.

### 05
This challenge involves pickle and its related processes called *pickling* and *unpickling*, which is serializing/deserializing a data object to/from a byte stream which could either be saved as a file or sent through the network. This is similar to the well-known and widely used JSON format and the processes associated to it. 

The *pickle* library is used to read the provided `.p` file and deserialize it to Python data objects. The resulting data object contains tuples within arrays within arrays. These tuples are of the form `('{char}', '{amount}')`, where `char` is the character to be printed out and `amount` is the number of times the character should be printed consecutively. Printing these characters as specified, along multiple lines, will show an ASCII art of the answer.

### 06
This challenge is similar to challenge #04, where a trail of **"nothing"** values are followed. However, these **"nothing"** values are contained in separate `.txt` files inside a `.zip` file, with the `readme.txt` file containing the first **"nothing"** value.

The *zipfile* library is used to open the zip file and easily navigate and open the `.txt` files contained within it. Following the trail of **"nothing"** values will result in another hint to "collect the comments." 

It is possible to comment files within a zip file, and these comments can be collected using `file.getinfo().comment`. Printing out these collection of comments will show another ASCII art that shows the answer.
