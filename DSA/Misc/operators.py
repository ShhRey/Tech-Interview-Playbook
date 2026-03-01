
"""
#============================================== Operator Precendence and Associativity in Python =======================================================#

  Operator Symbol Precedence (Up to Down)               What are the Matching Operators Used For                         Associativity Direction       
    ()                                                    Paranthesis                                                             L2R
    **                                                    Exponent / Power                                                   Right to Left
    +x, -x, ~x                                            Unary Plus/Minus, Bitwise NOT                                           L2R 
    *  /  //  %                                           Multiply, Divide, Floor Div, Modulus                                    L2R 
    +  -                                                  Addition, Subtraction                                                   L2R 
    <<  >>                                                LSHIFT,  RSHIFT                                                         L2R  
    &                                                     Bitwise AND                                                             L2R  
    ^                                                     Bitwise XOR                                                             L2R  
    |                                                     Bitwise OR                                                              L2R  
    == != < <= > >= is is-not in not-in                   Comparison, Identity, Membership                                        L2R 
    NOT                                                   Logical NOT                                                             L2R  
    AND                                                   Logical AND                                                             L2R     
    OR                                                    Logical OR                                                              L2R 
    =  +=  -=  *=  /=                                     Assignment Operators                                               Right to Left                 
    



 
#====================================================== Arithmetic Operators ===============================================#
They are one of the most basic operators, used to perform basic day-to-day tasks.
There are seven arithmetic operators:

=> Addition                   +           a + b           total of two numbers
=> Subtraction                -           a - b           difference between two numbers
=> Multiplication             *           a * b           product of two numbers
=> Division                   /           a / b           division of two numbers (float)
=> Floor Division             //          a // b          ignore decimal and rounds down to the nearest whole number
=> Modulus                    %           a % b           returns the remainder while performing division
=> Exponentiation             **          a ** b          multiplies a with itself b times





#================================================= Logical Operators ======================================================#
They are used to combine multiple conditions or expressions together and produce a Boolean result.
They are mainly used in control statements. There are three logical operators:

=> and              returns True if both operands are True, otherwise returns False  
=> or               returns True if atleast any one of the operand is True, else returns False
=> not              returns opposite boolean value of the operand





#=========================================================================== Comparison Operators ==========================================================================#
They are used to compare two values and return a Boolean value depending on the result of the comparison.
There are six comparison operators:

=> equal to                     (==)                returns True if values on both sides are equal, otherwise False
=> not equal to                 (!=)                returns True of values on both sides are not equal, otherwise False
=> less than                    (<)                 returns True if value on the left of operator is less than value on right, otherwise False
=> less than equal to           (<=)                returns True if value on the left of operator is less than or equal to value on right, otherwise False                  
=> greater than                 (>)                 returns True if value on the right of operator is greather than value on right, otherwise False                 
=> greater than equal to        (>=)                returns True if value on the right of operator is greater than or equal to value on right, otherwise False





#=============================================================================== Bitwise Operators ==================================================================================#
They are used to perform operations on individual bits of binary numbers.
There are six bitwise operators: 

=> Bitwise AND                  &                   returns 1 only when bits on both sides of operand are 1, otherwise 0                   
=> Bitwise OR                   |                   returns 1 when bits on either side of operand are 1, otherwise 0
=> Bitwise NOT                  ~                   returns complement of the input by flipping every bit (1 becomes 0, and visa-versa)
=> Bitwise XOR                  ^                   returns 1 when bits on both sides of operand are different, otherwise 0  
=> Bitwise LSHIFT               <<                  returns a value where bits of left operand are moved to the left, by the number of position as specified by the right operand           
=> Bitwise RSHIFT               >>                  returns a value where bits of left operand are moved to the right, by the number of position as specified by the right operand

Evaluated in the following precedence:  [ ~       << >>   &    ^     | ]





#============================================== Identity Operators =====================================================#
These are used to check whether two objects are of same type, and are stored in same memory location or not.
There are two identity operators:

=> is                       returns True if both variables point to the same object, otherwise False   
=> is-not                   returns True if both variables point to different objects, otherwise False





#=============================================== Membership Operators =================================================#
They are used to test whether a specific value or item is present in a sequence (string, list, tuple, set) or not.
There are two membership operators:

=> in                       returns True if the value is found in the sequence, otherwise False
=> not-in                   returns True if the value is not found in the sequence, otherwise False
"""