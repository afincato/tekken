tekken
======

Fiddling w/ python to build ad-hoc views of my plain-text based `project.todo` files.

Meanwhile I put together less messy notes, the basic idea is:

* keep each project in its own `.txt` (or if you want `.md`) file
* use python’s `today` and `upcoming` scripts to build a text file that filters out and group together all tasks fitting that view
* print the same view also on a terminal window

## Basic syntax

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

* copy a list or a bunch of newlines from an email and format each new line / list-item as task-list-item w/ a shortcut (iaWriter can do it, I suppose neovim as well, emacs for sure)
* copy from `project.todo` and paste it somewhere, share it, send a message, etc.
* print it out on a piece of paper (stupid but useful)
* convert it back and forth from / to `json`! This is something I want to work on