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