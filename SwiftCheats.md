# Swift 3 Cheatsheet

## Syntax and style

- C-like syntax.
- Strong typing with type inference.
- CamelCase

```swift
{ ... scope ... }

class ClassName { // CamelCase
}
struct StructName { // K&R Braces
    let constantName = 0 // lowerCamelCase
    var variableName = 0 
}

doSomething()
doSomething(); // Semicolons are *optional* at end of statements

```

### Function naming

```swift
func makeSomething() -> Something
func isSomethingTrue -> Bool

extension List { 
  /// Include all the words needed to avoid ambiguity
  public mutating func remove(at position: Index) -> Element
  /// Remove needless words
  public mutating func remove(_ member: Element) -> Element?
}
employees.remove(at: x)
allViews.remove(cancelButton) // clearer

/// Name variables, parameters, and associated types according to their roles
func restock(from widgetFactory: WidgetFactory) // NO
func restock(from supplier: WidgetFactory) // YES

/// Compensate for weak type information to clarify a parameter’s role.
func add(_ observer: NSObject, for keyPath: String) // NO
func addObserver(_ observer: NSObject, forKeyPath path: String) // YES

/// Split long function names
func reticulateSplines(spline: [Double], adjustmentFactor: Double,
    translateConstant: Int, comment: String) -> Bool {
  // reticulate code goes here
}

```

### Commenting 

```swift
// Line
/* Block */
```

### Documenting

```swift
/*! or /** or /*:
 * - Markdown can be used
 */
 
//: Single line w. markdown
/// - parameter whateverParameter single line comment

/*! Description
 * @parameter paranName description
 * @return whatever 
 */
```

### MARK, TODO, FIXME... ("pragma mark")

```swift
// MARK:- Use mark to logically organize your code
// TODO:
// FIXME:
```

## Variables and constants

### Constants

**let** *constantName*[*:type*] = *value*

```swift
let constantName:Int = 3
let contatntNameInferred = 3 // Type is inferred
let (a,b,c) = (1,2,3)
```

### Variables

**var** *variableName*[*:type*][?] [ = *value*]

- *type* is optional if value is given.
- ? allows the variable to be nil.

```swift
var variableName:Int = 3
var variableNameInferred = 3 // Type is inferred
variableName = 4 // Assigning is ok

var optionalValue? = nil
if let strictlyValued = optionalValue {
	// Only if optionalValue != nil
}
```

## Types

### Basic types

* Int (1,2,3...)
* Float (1.0, 3.14,...)
* Double (1.0, 6.28,...)
* Bool (**true**, **false**)
* Character (**"\u{00E9}"**)
* String ("Hello world!", "", String())
* ClassName (UIButton, Potato...)
* Range (1...3, 1..<3)

### Type conversion

```swift
var aString = "1234"
var aInt = Int(aString)
var anotherString = "3.1415"
var aDouble = Double(anotherString)
```

## Strings

* String is a UTF container. 
* To access the string as a collection of characters, use the `.characters` property.
* Use `import Foundation` for all the usual ObjC goodness.

### String creation

```swift
var emptyString = ""            // Empty String
var stillEmpty = String()       // Another empty String
let helloWorld = "Hello World!" // String literal

let a = String(true)            // from boolean: "true"
let b: Character = "A"          // Explicit type to create a Character
let c = String(b)               // from character "A"
let d = String(3.14)            // from Double "3.14"
let e = String(1000)            // from Int "1000"
let f = "Result = \(d)"         // Interpolation "Result = 3.14"
let g = "\u{2126}"              // Unicode Ohm sign Ω
```

### String special characters

* Null Character: `\0`
* Backslash: `\\` (can be used to escape a double quote)
* Horizontal Tab: `\t`
* Line Feed: `\n`
* Carriage Return: `\r`
* Double Quote: `\"`
* Single Quote: `\'`
* Unicode scalar: `\u{n}` where n is between one and eight hexadecimal digits

#### Repeating String creation

```swift
let h = String(repeating:"01", count:3) // 010101
```

#### String from a file

```swift
if let txtPath = Bundle.main.path(forResource: "lorem", ofType: "txt") {
  do {
    let lorem = try String(contentsOfFile: txtPath, encoding: .utf8)
  } catch {
    print("Something went wrong")
  }
}
```

### String checks

#### String emptiness

```swift
var emptyString = ""
emptyString.isEmpty     // true
```

#### String Equality

```swift
print "a" == "a" // true
print "a" == "b" // false
```

#### String comparing for order:

```swift
if "aaa" < "bbb" {
  print("aaa is less than bbb")  // "aaa is less than bbb"
}
```

#### String Containment

```swift
var helloWorld = "Hello world!"
print helloWorld.rangeOfString("Foo") // nil
```

#### String testing for suffix/prefix

```swift
let line = "0001 Some test data here %%%%"
line.hasPrefix("0001")    // true
line.hasSuffix("%%%%")    // true
```

### String Character counting and Looping

```swift
var myString="Hello world!"
let len = myString.characters.count 
for ch in myString.characters {
	print(ch)
}

for (i, c) in "hello".characters.enumerated() {
    print("\(i): \(c)")
}
/* Prints:
0: h
1: e
2: l
3: l
4: o
*/
```

#### String characters are *grapheme clusters*.

```swift
let single = "Pok\u{00E9}mon"
let double = "Pok\u{0065}\u{0301}mon" // They both display identically:

(single, double) // → (.0 "Pokémon", .1 "Pokémon")
// And both have the same character count:
single.characters.count // → 7
double.characters.count // → 7

// Only if you drop down to a view of the underlying representation can you see that they are different:

single.utf16.count // → 7
double.utf16.count // → 8
```

#### String Views

```swift
country.characters       // characters
country.unicodeScalars   // Unicode scalar 21-bit codes
country.utf16            // UTF-16 encoding
country.utf8             // UTF-8 encoding
```

#### Counting

```swift
// spain = España
print("\(spain.characters.count)")      // 6
print("\(spain.unicodeScalars.count)")  // 6
print("\(spain.utf16.count)")           // 6
print("\(spain.utf8.count)")            // 7
```

### String manipulation

#### String Concatenation

```swift
var x = "a" + "b"
var y = x.append(Character("c"))
```

#### String Interpolation

```swift
var world = "world"
var hello = "Hello"
var helloWorld = "\(hello) \(world)!"
```

#### String Prefix, suffix

```swift
var pref = String("abcdefg".characters.prefix(4)) // abcd 
```

#### String Finding and Inserting

```swift
var hello = "Hello!"
if let idx = hello.characters.index(of: "!") {
    hello.insert(contentsOf: ", world".characters, at: idx)
}
```

#### Converting to upper/lower case

```swift
let mixedCase = "AbcDef"
let upper = mixedCase.uppercased() // "ABCDEF"
let lower = mixedCase.lowercased() // "abcdef"
```

## Files

### UserDefaults

```swift
let userDefaults = UserDefaults.standard
userDefaults.setValue("Some Value", forKey: "RPSomeUserPreference")
let userDefaults = UserDefaults.standard
let someValue = userDefaults.value(forKey: "RPSomeUserPreference") as AnyObject?
```

###  Reading

```swift
    do {
        let text = try String(contentsOf: url, encoding: String.Encoding.utf8)
    }
    catch {/* error handling here */}

```

* To use a String path, use `contentsOfFile:path`

### Writing

```swift
    let text = "Some text"
    do {
        try text.write(to: url, atomically: false, encoding: String.Encoding.utf8)
    }
    catch {/* error handling here */}
```

## Objects and Classes

### Primitives

**nil** : Used to specify a null object pointer.  When classes are first initialized, all properties of the class point to `nil`.

### Classes, Structure, Functions and Protocols

Directive | Purpose
:---: | ---
| typealias | Introduces a named alias of an existing type
| enum | Introduces a named enumeration
| struct | Introduces a named structure
| class | Begins the declaration of a class
| init | Introduces an initializer for a class, struct or enum
| init? | Produces an optional instance or an implicitly unwrapped optional instance; can return `nil`
| deinit | Declares a function called automatically when there are no longer any references to a class object, just before the class object is deallocated
| func | Begins the declaration of a function
| protocol | Begins the declaration of a formal protocol
| static | Defines as type-level within struct or enum
| convenience | Delegate the init process to another initializer or to one of the class’s designated initializers
| extension | Extend the behavior of class, struct, or enum
| subscript | Adds subscripting support for objects of a particular type, normally for providing a convenient syntax for accessing elements in a collective, list or sequence
| override | Marks overriden initializers

### Patterns: Delegation

* When creating custom delegate methods, an unnamed first parameter should be the delegate source. (UIKit contains numerous examples of this.)

```swift
func namePickerView(_ namePickerView: NamePickerView, didSelectName name: String)
func namePickerViewShouldReload(_ namePickerView: NamePickerView) -> Bool
```

### Patterns: Singleton

```swift
class MyClass {
    static let sharedInstance = MyClass()   
    fileprivate init() {}
}
let myClass = MyClass.sharedInstance

```

### Enum & Bitmask Types

```swift
// Specifying a typed enum with a name (recommended way)
enum UITableViewCellStyle: Int {
    case default, valueOne, valueTwo, subtitle
}

// Accessing it:
let cellStyle: UITableViewCellStyle = .default
```

#### Working with Bitmasks

```swift
struct Options: OptionSet {
    let rawValue: Int
    
    init(rawValue: Int) {
        self.rawValue = rawValue
    }
    
    init(number: Int) {
        self.init(rawValue: 1 << number)
    }
    
    static let OptionOne = Options(number: 0)
    static let OptionTwo = Options(number: 1)
    static let OptionThree = Options(number: 2)
}

let options: Options = [.OptionOne, .OptionTwo]

options.contains(.OptionOne) // true
options.contains(.OptionThree) // false
```

### Type Casting

#### Checking Types

```swift
if item is Movie {
    movieCount += 1
    print("It is a movie.")
} else if item is Song {
    songCount += 1
    print("It is a song.")
}

```

#### Operators: as? and as!

```swift
for item in library {
    if let movie = item as? Movie {
        print("Director: \(movie.director)")
    } else if let song = item as? Song {
        print("Artist: \(song.artist)")
    }
}
```

#### Casting from Generic Types

```swift
var someObjects = [Any]()

for movie in someObjects as! [Movie] {
    // do stuff
}
```


```swift
var things = [Any]()

for thing in things {
    switch thing {
    case 0 as Int:
        print("Zero as an Int")
    case let someString as! String:
        print("S string value of \"\(someString)\"")
    case let (x, y) as! (Double, Double):
        print("An (x, y) point at \(x), \(y)")
    case let movie as! Movie:
        print("A movie called '\(movie.name)' by director \(movie.director)")
    default:
        print("Didn't match any of the cases specified")
    }
}
```

#### Basic Casting

```swift
// Example 1:
let aDifferentDataType: Float = 3.14
let anInt: Int = Int(aDifferentDataType)

// Example 2:
let aString: String = String(anInt)
```

## Operators

#### Arithmetic Operators

Operator | Purpose
:---: | ---
| + | Addition
| - | Subtraction
| * | Multiplication
| / | Division
| % | Remainder

#### Comparative Operators

Operator | Purpose
:---: | ---
| == | Equal to
| === | Identical to
| != | Not equal to
| !== | Not identical to
| ~= | Pattern match, also "is in range", e.g. 1..<3 ~= 2
| > | Greater than
| < | Less than
| >= | Greater than or equal to
| <= | Less than or equal to

#### Assignment Operators

Operator | Purpose
:---: | ---
| = | Assign
| += | Addition
| -= | Subtraction
| *= | Multiplication
| /= | Division
| %= | Remainder
| &= | Bitwise AND
| &#124;= | Bitwise Inclusive OR
| ^= | Exclusive OR
| <<= | Shift Left
| >>= | Shift Right

#### Logical Operators

Operator | Purpose
:---: | ---
| ! | NOT
| && | Logical AND
| &#124;&#124; | Logical OR

#### Range Operators

Operator | Purpose
:---: | ---
| ..< | Half-open range
| ... | Closed range

#### Bitwise Operators

Operator | Purpose
:---: | ---
| & | Bitwise AND
| &#124; | Bitwise Inclusive OR
| ^ | Exclusive OR
| ~ | Unary complement (bit inversion)
| << | Shift Left
| >> | Shift Right

#### Overflow and Underflow Operators

Operator | Purpose
:---: | ---
| &+ | Addition
| &- | Subtraction
| &* | Multiplication

```swift
var willOverflow = UInt8.max
// willOverflow equals 255, which is the largest value a UInt8 can hold
willOverflow = willOverflow &+ 1
// willOverflow is now equal to 0

var willUnderflow = UInt8.min
// willUnderflow equals 0, which is the smallest value a UInt8 can hold
willUnderflow = willUnderflow &- 1
// willUnderflow is now equal to 255
```

#### Other Operators

Operator | Purpose
:---: | ---
| ?? | Nil coalescing
| ?: | Ternary conditional
| ! | Force unwrap object value
| ? | Safely unwrap object value

## Operator Overloading

* Limited to `/ = - + * % < > ! & | ^ . ~`. 
* Cannot overload `=` operator by itself (it must be combined with another symbol).
* `prefix`: goes before an object such as `-negativeNumber`
* `infix`: goes between two objects, such as `a + b`
* `postfix`: goes after an object, such as `unwrapMe!`
Examples:

```swift
struct Vector2D: CustomStringConvertible {
    var x = 0.0, y = 0.0
    
    var description: String {
        return "Vector2D(x: \(x), y: \(y))"
    }
}

infix operator +-: AdditionPrecedence
extension Vector2D {
    static func +- (left: Vector2D, right: Vector2D) -> Vector2D {
        return Vector2D(x: left.x + right.x, y: left.y - right.y)
    }
}
let firstVector = Vector2D(x: 1.0, y: 2.0)
let secondVector = Vector2D(x: 3.0, y: 4.0)
let plusMinusVector = firstVector +- secondVector
// plusMinusVector is a Vector2D instance with values of (4.0, -2.0)
```

## Preprocessor

Directive | Purpose
:---: | ---
| #if | An `if` conditional statement
| #elif | An `else if` conditional statement
| #else | An `else` conditional statement
| #endif | An `end if` conditional statement

### Imports

Directive | Purpose
:---: | ---
| import | Imports a framework



#### Operators

Directive | Purpose
:---: | ---
| operator | Introduces a new infix, prefix, or postfix operator

#### Declaration Modifiers

Directive | Purpose
:---: | ---
| dynamic | Marks a member declaration so that access is always dynamically dispatched using the Objective-C runtime and never inlined or devirtualized by the compiler
| final | Specifies that a class can’t be subclassed, or that a property, function, or subscript of a class can’t be overridden in any subclass
| lazy | Indicates that the property’s initial value is calculated and stored at most once, when the property is first accessed
| optional | Specifies that a protocol’s property, function, or subscript isn’t required to be implemented by conforming members
| required | Marks the initializer so that every subclass must implement it
| weak | Indicates that the variable or property has a weak reference to the object stored as its value

#### Access Control

Directive | Purpose
:---: | ---
| open | Can be subclassed outside of its own module and its methods overridden as well; truly open to modification by others and useful for framework builders
| public | Can only be subclassed by its own module or have its methods overridden by others within the same module
| internal | (Default) Indicates the entities are only available to the entire module that includes the definition, e.g. an app or framework target
| fileprivate | Indicates the entities are available only from within the source file where they are defined
| private | Indicates the entities are available only from within the declaring scope within the file where they are defined (e.g. within the `{ }` brackets only)


## Literals

Literals are compiler directives which provide a shorthand notation for creating common objects.

Syntax | What it does
:---: | ---
| `"string"` | Returns a `String` object
| `28` | Returns an `Int`
| `3.14`, `0xFp2`, `1.25e2` | Returns a `Float` object
| `true`, `false` | Returns a `Bool` object
| `[]` | Returns an `Array` object
| `[keyName:value]` | Returns a `Dictionary` object
| `0b` | Returns a binary digit
| `0o` | Returns an octal digit
| `0x` | Returns a hexadecimal digit

## Functions

### Declaration Syntax

Functions without a return type use this format:

```swift
// Does not return anything or take any arguments
func doWork() {
    // Code
}
```

`class` precedes declarations of class functions:

```swift
// Call on a class, e.g. MyClass.someClassFunction()
class func someClassFunction() {
    // Code
}
```

`static` is similar to class functions where you don't need an instance of the class or struct in order to call a method on it:

```swift
// Call on a class/struct, e.g. MyStruct.someStaticFunction()
static func someStaticFunction() {
    // Code
}
```

Declare instance functions:

```swift
// Called on an instance of a class, e.g. myClass.someInstanceFunction()
func doMoreWork() {
    // Code
}
```

Function arguments are declared within the parentheses:

```swift
// Draws a point
func draw(point: CGPoint)
```

Return types are declared as follows:

```swift
// Returns a String object for the given String argument
func sayHelloToMyLilFriend(lilFriendsName: String) -> String {
    return "Oh hello, \(lilFriendsName). Cup of tea?"
}
```

You can have multiple return values, referred to as a tuple:

```swift
// Returns multiple objects
func sayHelloToMyLilFriend(lilFriendsName: String) -> (msg: String, nameLength: Int) {
    return ("Oh hello, \(lilFriendsName). Cup of tea?", countElements(lilFriendsName))
}

var hello = sayHelloToMyLilFriend("Rob")
print(hello.msg) // "Oh hello, Rob. Cup of tea?"
print(hello.nameLength) // 3
```

And those multiple return values can be optional:

```swift
func sayHelloToMyLilFriend(lilFriendsName: String) -> (msg: String, nameLength: Int)?
```

By default, external parameter names are given when you call the function, but you can specify that one or more are not shown in the method signature by putting a `_` symbol in front of the parameter name:

```swift
func sayHelloToMyLilFriend(_ lilFriendsName: String) {
    // Code
}

sayHelloToMyLilFriend("Rob")
```

or you can rename the variable once within the method scope:

```swift
func sayHelloToMyLilFriend(friendsName lilFriendsName: String) {
    // Code
}

sayHelloToMyLilFriend(friendsName: "Rob") // and local variable is `lilFriendsName`
```


You can also specify default values for the parameters:

```swift
func sayHelloToMyLilFriend(_ lilFriendsName: String = "Rob") {
    // Code
}

sayHelloToMyLilFriend() // "Oh hello, Rob. Cup of tea?"
sayHelloToMyLilFriend("Jimbob") // "Oh hello, Jimbob. Cup of tea?"
```

Swift also supports variadic parameters so you can have an open-ended number of parameters passed in:

```swift
func sayHelloToMyLilFriends(_ lilFriendsName: String...) {
    // Code
}

sayHelloToMyLilFriends("Rob", "Jimbob", "Cletus")
// "Oh hello, Rob, Jimbob and Cletus. Cup of tea?"
```

And lastly, you can also use a prefix to declare input parameters as `inout`.

An in-out parameter has a value that is passed in to the function, is modified by the function, and is passed back out of the function to replace the original value.

You may remember `inout` parameters from Objective-C where you had to sometimes pass in an `&error` parameter to certain methods, where the `&` symbol specifies that you're actually passing in a pointer to the object instead of the object itself. The same applies to Swift's `inout` parameters now as well.

#### Calling Functions

Functions are called using dot syntax: `myClass.doWork()` or `self.sayHelloToMyLilFriend("Rob Phillips")`

`self` is a reference to the function's containing class.

At times, it is necessary to call a function in the superclass using `super.someMethod()`.

## Constants and Variables

Declaring a constant or variable allows you to maintain a reference to an object within a class or to pass objects between classes.

Constants are defined with `let` and variables with `var`. By nature, constants are obviously immutable (i.e. cannot be changed once they are instantiated) and variables are mutable.

```swift
class MyClass {
	let text = "Hello" // Constant
	var isComplete: Bool // Variable
}
```

There are many ways to declare properties in Swift, so here are a few examples:

```swift
var myInt = 1 // inferred type
var myExplicitInt: Int = 1 // explicit type
var x = 1, y = 2, z = 3 // declare multiple variables

let (a,b) = (1,2) // declare multiple constants
```

#### Access Levels

The default access level for constants and variables is `internal`:

```swift
class MyClass {
    // Internal (default) properties
	var text: String
	var isComplete: Bool
}
```

To declare them publicly or openly, they should also be within a `public` or `open` class as shown below:

```swift
public class MyClass {
    // Public properties
	public var text: String
	public let x = 1
}

// Or

open class MyClass {
    // Public properties
	open var text: String
	open let x = 1
}
```

File private variables and constants are declared with the `fileprivate` directive:

```swift
class MyClass {
    // Private properties
	fileprivate var text: String
	fileprivate let x = 1
}
```

#### Getters and Setters

In Objective-C, variables were backed by getters, setters, and private instance variables created at build time. However, in Swift getters and setters are only used for computed properties and constants actually don't have a getter or setter at all.

The getter is used to read the value, and the setter is used to write the value. The setter clause is optional, and when only a getter is needed, you can omit both clauses and simply return the requested value directly. However, if you provide a setter clause, you must also provide a getter clause.

You can overrride the getter and setter of a property to create the illusion of the Objective-C property behavior, but you'd need to store them as a private property with a different name (not recommended for most scenarios):

```swift
private var _x: Int = 0

var x: Int {
    get {
        print("Accessing x...")
        return _x
    }
    set {
        print("Setting x...")
        _x = newValue
    }
}
```

#### Access Callbacks

Swift also has callbacks for when a property will be or was set using `willSet` and `didSet` shown below:

```swift
var numberOfEdits = 0
var value: String = "" {
    willSet {
        print("About to set value...")
    }
    didSet {
        numberOfEdits += 1
    }
}
```

#### Accessing

Properties can be accessed using dot notation:

```swift
myClass.myVariableOrConstant
self.myVariable // Self is optional here except within closure scopes
```

#### Local Variables

Local variables and constants only exist within the scope of a function.

```swift
func doWork() {
    let localStringVariable = "Some local string variable."
    self.doSomething(string: localStringVariable)
}
```

[Back to top](#swift-3-cheat-sheet)

## Naming Conventions

The general rule of thumb: Clarity and brevity are both important, but clarity should never be sacrificed for brevity.

#### Functions and Properties

These both use `camelCase` where the first letter of the first word is lowercase and the first letter of each additional word is capitalized.

#### Class names and Protocols

These both use `CapitalCase` where the first letter of every word is capitalized.

### Enums

The options in an enum should be `lowerCamelCased`

#### Functions

These should use verbs if they perform some action (e.g. `performInBackground`).  You should be able to infer what is happening, what arguments a function takes, or what is being returned just by reading a function signature.

Example:

```swift
// Correct
func move(from start: Point, to end: Point) {}

// Incorrect (likely too expressive, but arguable)
func moveBetweenPoints(from start: Point, to end: Point) {}

// Incorrect (not expressive enough and lacking argument clarity)
func move(x: Point, y: Point) {}
```

[Back to top](#swift-3-cheat-sheet)

## Closures

Closures in Swift are similar to blocks in Objective-C and are essentially chunks of code, typically organized within a `{}` clause, that are passed between functions or to execute code as a callback within a function. Swift's `func` functions are actually just a special case of a closure in use.

#### Syntax

```swift
{ (params) -> returnType in
    statements
}
```

#### Examples

```swift
// Map just iterates over the array and performs whatever is in the closure on each item
let people = ["Rob", "Jimbob", "Cletus"]
people.map({
    (person: String) -> String in
    "Oh hai, \(person)..."
})
// Oh hai, Rob
// Oh hai, Jimbob
// Oh hai, Cletus

// Closure for alphabetically reversing an array of names, where sorted is a Swift library function
let names = ["Francesca", "Joe", "Bill", "Sally", ]
var reversed = names.sorted { (s1: String, s2: String) -> Bool in
    return s1 > s2
}
// Or on a single line:
reversed = names.sorted{ (s1: String, s2: String) -> Bool in return s1 > s2 }
// Or because Swift can infer the Bool type:
reversed = names.sorted { s1, s2 in return s1 > s2 }
// Or because the return statement is implied:
reversed = names.sorted { s1, s2 in s1 > s2 }
// Or even shorter using shorthand argument names, such as $0, $1, $2, etc.:
reversed = names.sorted { $0 > $1 }
// Or just ridiculously short because Swift's String greater-than operator implementation exactly matches this function definition:
reversed = names.sorted(by: >)
```

If the closure is the last parameter to the function, you can also use the trailing closure pattern. This is especially useful when the closure code is especially long and you'd like some extra space to organize it:

```swift
func someFunctionThatTakesAClosure(closure: () -> ()) {
    // function body goes here
}

// Instead of calling like this:
someFunctionThatTakesAClosure({
    // closure's body goes here
})

// You can use trailing closure like this:
someFunctionThatTakesAClosure() {
    // trailing closure's body goes here
}
```
#### Capturing Values

A closure can capture constants and variables from the surrounding context in which it is defined. The closure can then refer to and modify the values of those constants and variables from within its body, even if the original scope that defined the constants and variables no longer exists.

In Swift, the simplest form of a closure that can capture values is a nested function, written within the body of another function. A nested function can capture any of its outer function’s arguments and can also capture any constants and variables defined within the outer function.

```swift
func makeIncrementor(forIncrement amount: Int) -> () -> Int {
    var runningTotal = 0
    func incrementor() -> Int {
        runningTotal += amount
        return runningTotal
    }
    return incrementor
}
```

Swift determines what should be captured by reference and what should be copied by value. You don’t need to annotate a variable to say that they can be used within the nested function. Swift also handles all memory management involved in disposing of variables when they are no longer needed by the function.

#### Capturing Self

If you create a closure that references `self.*` it will capture `self` and retain a strong reference to it. This is sometimes the intended behavior, but often could lead to retain cycles where both objects won't get deallocated at the end of their lifecycles.

The two best options are to use `unowned` or `weak`. This might look a bit messy, but saves a lot of headache.

Use `unowned` when you know the closure will only be called if `self` still exists, but you don't want to create a strong (retain) reference.

Use `weak` if there is a chance that `self` will not exist, or if the closure is not dependent upon `self` and will run without it. If you do use `weak` also remember that `self` will be an optional variable and should be checked for existence.

```swift
typealias SomeClosureType = (_ value: String) -> ()

class SomeClass {
    fileprivate var currentValue = ""

    init() {
        someMethod { (value) in // Retained self
            self.currentValue = value
        }
        
        someMethod { [unowned self] (value) in // Not retained, but expected to exist
            self.currentValue = value
            
        }
        
        someMethod { [weak self] value in // Not retained, not expected to exist
            // Or, alternatively you could do
            guard let sSelf = self else { return }
            
            // Or, alternatively use `self?` without the guard
            sSelf.currentValue = value
        }
    }
    
    func someMethod(closure: SomeClosureType) {
        closure("Hai")
    }
}
```

### Capture extending object lifetime

```swift
resource.request().onComplete { [weak self] response in
  guard let strongSelf = self else {
    return
  }
  let model = strongSelf.updateModel(response)
  strongSelf.updateUI(model)
}
```

## Control Statements

Swift uses all of the same control statements that other languages have:

#### If-Else If-Else

```swift
if someTestCondition {
    // Code to execute if the condition is true
} else if someOtherTestCondition {
    // Code to execute if the other test condition is true
} else {
    // Code to execute if the prior conditions are false
}
```

As you can see, parentheses are optional.

#### Ternary Operators

The shorthand notation for an `if-else` statement is a ternary operator of the form: `someTestCondition ? doIfTrue : doIfFalse`

Example:

```swift
func stringForTrueOrFalse(trueOrFalse: Bool) -> String {
    return trueOrFalse ? "True" : "False"
}
```

#### For Loops

Swift enables you to use ranges inside of `for` loops now:

```swift
for index in 1...5 {
    print("\(index) times 5 is \(index * 5)")
}

// Or if you don't need the value of the index
let base = 3, power = 10
var answer = 1
for _ in 1...power {
    answer *= base
}
print("\(base) to the power of \(power) is \(answer)")
// prints "3 to the power of 10 is 59049"
```


#### Enumerating arrays & dictionaries

```swift
// We explicitly cast to the Movie class from AnyObject class
for movie in someObjects as [Movie] {
    // Code to execute each time
}

// Enumerating simple array
let names = ["Anna", "Alex", "Brian", "Jack"]
for name in names {
    print("Hello, \(name)!")
}

// Enumerating simple dictionary
let numberOfLegs = ["spider": 8, "ant": 6, "cat": 4]
for (animalName, legCount) in numberOfLegs {
    print("\(animalName)s have \(legCount) legs")
}
```

If you need to cast to a certain object type, see the earlier discussion about the `as!` and `as?` keywords.

#### While Loop

```swift
while someTestCondition {
   // Code to execute while the condition is true
}
```

#### Repeat While Loop

```swift
repeat {
    // Code to execute while the condition is true
} while someTestCondition
```

