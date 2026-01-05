# Sjoerd Wouters

Welcome to my website

# This is a Heading h1
## This is a Heading h2
### This is a Heading h3
#### This is a Heading h4
##### This is a Heading h5
###### This is a Heading h6

This text will be normal
**This text will be bold**

## Tables

| Term:                           | Syntax:                            | Calls:                                    |
| ------------------------------- | -----------------------------------|------------------------------------------ |
| **Direct Initialization**       | ``Type x(value);``                 | constructor                               |
| **Direct Brace Initialization** | ``Type x{value};``                 | constructor or initializer list           |
| **Copy Brace Initialization**   | ``Type x = {value};``              | constructor or initializer list           |
| **Copy Initialization**         | ``Type x = value;``                | copy constructor                          |
| **Move Initialization**         | ``Type x = std::move(value);``     | move constructor                          |
| **Copy Assignment**             | ``x = value;``                     | copy operator (not initialization)        |
| **Move Assignment**             | ``x = std::move(value);``          | move operator (not initialization)        |

## Blocks of code

```csharp
// csharp
void Example(Class instance)
{
    // changes the original instance
    instance.variable = 1;

    int x = 4 * 5;

    // this creates a copy
    Class instance_copy = instance.Clone();
}
```

```cpp
// cpp
void Example(Class& instance)
{
    // changes the original instance
    instance.variable = 1;

    int x = 4 * 5;

    // this creates a copy
    Class instance_copy = instance;
}
```

## Inline code

This is inline code `testcode`.

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz