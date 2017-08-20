tekken
======

Fiddling w/ python to build ad-hoc views of my plain-text based `project.todo` files.

Meanwhile I put together less messy notes, the basic idea is:

* keep each project in its own `.txt` (or if you want `.md`) file
* use python’s `today` and `upcoming` scripts to build a text file that filters out and group together all tasks fitting that view
* print the same view also on a terminal window

## Basic syntax

| syntax             | meaning         |                            
|:--                 |:--              |
| `- [ ]`            | undone task     |
| `- [x]`            | done task       |
| `@due(dd-mm-yyyy)` | due date        |
| `*`                | starred task    |
| `## section`       | section divider |

Example

```
# nein @due(20-08-2017) #project

## general

- [x] test *

## ahah *

- [x] make nothing @due(20-08-2017)
- [ ] nah @due(20-08-2017)
- [ ] ehh *
- [ ] don’t @due(20-08-2017)

```

Adding `@due(dd-mm-yyyy)` and `*` to a `## section` is also possible: it will grab all containing items and will put them in `today.todo.txt`.
 
## Portability

With plain text files you can do any kind of text-manipulation, eg:

* copy a list or a bunch of newlines from an email and format each new line / list-item as task-list-item w/ a shortcut (iaWriter can do it, I suppose neovim as well, emacs for sure)
* copy from `project.todo` and paste it somewhere, share it, send a message, etc.
* print it out on a piece of paper (stupid but useful)
* convert it back and forth from / to `json`! This is something I want to work on