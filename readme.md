tekken
======

## Syntax

| syntax             | meaning           |                            
|:--                 |:--                |
| `- [ ]`            | undone task       |
| `- [x]`            | done task         |
| `- [c]`            | cancelled task    |
| `- [w]`            | waiting task      |
| `s(ddmmyyyy)`      | scheduled task    |
| `d(ddmmyyyy)`      | deadline for task |
| `d(t)`             | deadline today    |
| `## section`       | section divider   |

Example

```
## general

- [x] test d(t)
- [w] toast

## ahah

- [x] make nothing d(20082017)
- [ ] nah s(20082017)
- [c] ehh
```
 
## Portability

With plain text files you can do any kind of text-manipulation, eg:

- copy a list or a bunch of newlines from an email and format each new line / list-item as task-list-item w/ a shortcut
- copy from `project.todo` and paste it somewhere, share it, send a message, etc.
- print it out on a piece of paper (stupid but useful)
- convert it back and forth from / to different format by implementing an AST