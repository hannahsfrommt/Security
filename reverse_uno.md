
Stack - A group of memory locations; a reserved part of memory used by programmers
General Register - A multipurpose register that can be used by either programmer or user to store data or a memory location address


|     |        X86_64 Assembly - Common Instruction Pointers                 |
|-----|----------------------------------------------------------------------|
| MOV | move source to destination 
| PUSH | push source onto stack 
| POP | Pop top of stack to destination 
| INC | Increment source by 1 
| DEC | Decrement source by 1 
| ADD | Add source to destination
| SUB | Subtract source from destination
| CMP | Compare 2 values by subtracting them and setting the %RFLAGS register. ZeroFlag set means they are the same.
| JMP | Jump to specified location
| JLE | Jump if less than or equal
| JE | Jump if equal








```
main:
    mov rax, 16     //16 moved into rax
    push rax        //push value of rax (16) onto stack. RSP is pushed up 8 bytes (64 bits)
    jmp mem2        //jmp to mem2 memory location

mem1:
    mov rax, 0      //move 0 (error free) exit code to rax
    ret             //return out of code

mem2:
    pop r8          //pop value on the stack (16) into r8. RSP falls 8 bytes
    cmp rax, r8     //compare rax register value (16) to r8 register value (16)
    je mem1         //jump if comparison has zero bit set to mem1
```
