# dot-todo

## for a critique of plain-text todo: apps, syntaxes, intents, usages

I could just stick to any ‘proper’ task management application, in the best case using a database of some sort, and stick with it.

Instead, last summer, in a moment of total euphoria for plain text files and the capabilities they way to manage data (replacing databases in many occasions), I moved from Things.app to Taskpaper.

Unfortunately, Taskpaper is a decente app with a brilliant syntax. I still don’t get why, after almost ten years since its first version, to get reminders and recurrent tasks, YOU-HAVE-TO-USE external scripts against your Taskpaper file. Meaning you have to use other applications to run these scripts the smoother and effortlessly you can, in order to have basic options running.

It’s for sure a clear decision from the dev team making the app, and I don’t get it. Nevermind.

I am right now in the process of looking around again, as I like plain-text files as a format to keep my todos, and I think the syntax from Taskpaper covers quite well many options, but Taskpaper feels too much like text. You can drag a task around, but only by clicking on the tiny dot next to the beginning of the task. That’s pretty unusable.

I quickly converted my todos to the todo.txt format, and played with Swiftodo, a new iOS app supporting this project.

I quite like you tag each and every todo as if it was on its on, not visually belonging to a project (eg by way of indentation), and the syntax is way more compact (though limited).

Still, I think it makes no sense having to manually add to each and every tasks to which project they belong to: once you indent them below a line ending with a colon, that should become a tag.

I might change my mind again very soon, but for sure it felt a bit too tedious after a bit having to treat each task as an independent atom. It sure is like one, I’m only thinking about this could be managed more effortlessly.

In general though, I think there exist a rich syntax from which to draw from, as what I am writing is an outline for a new, or rather, another format and syntax for keeping todo files.

My first and main gripe with both projects (and relative syntaxes), is that nowadays using a simple dash, or no dash at all, to indicate a new task, is just confusing. It’s not because they ask you to keep your todo file on its own, but I want to be able to use a more general purpose approach to this, and delineate a new task by using github’s syntax suggestion:

`- [ ]`

and 

`1. [ ]`

Only using `[ ]` might not be clear enough that it’s part of a list. Sure, this is a bit more verbose maybe, but it’s more explicit, to you and to your general markdown usage. You can mix things up, jot down new notes and add a bunch of todos, before copy-pasting or just cut-pasting them into this new… app?

Anyway, using `- [ ]` is also visually more clear, especially when you complete a task and what you see is `- [x]`.

Github introduced this syntax some years ago, I think it fits very well into markdown and as a strategy to write an updated syntax for plain-text todo files.

### What else to borrow from takspaper’s and todo.txt’s syntaxes?

I would personally replace either `@tag` (Taskpaper) and `+tag` (todo.txt), and would go for `#tag`. Does it mess with markdown? A bit, maybe. But at the same time it matches with markdown, as if `# headers` are a way to mark sections in a text, `#tags` are too. Just don’t put a space between the hashtag and the tag, and you’re done.

Still, I like to use `@` for contexts. And I use contexts for grouping things together on a more overarching level, beside `@home` and `@work` (what do they mean nowadays, anyway), I might use `@project` if I know this is a big project, or a long-running project, for which I might do a series of projects under it.

For due dates, `@` is also excellent: add a parentheses and place a date—`@due(2017-08-15)`.

Taskpaper has a quick date drawer that you can use to insert *natural language date*, and once you write `next monday` and press `enter`, it transforms it into `yyyy-mm-dd`. Is it as readable as having `next monday`, probably not. But that’s a problem you can solve at least in one way: by having an app that reads that date and convert it to a relative date (`next monday`), and if some days are passed and now Monday has become tomorrow, it should show you `tomorrow`.

The other time-based option is for recurrent task (in a fork of todo.txt CLI this option is apparently implemented, still did not test personally). Often people say that’s what you use a calendar for, and I might agree in many instances, but I sometimes, for specific stuff, want to be able to have an iterable reminder. Nothing else.

Another thing to borrow from taskpaper, is adding notes within that task. Like:

	# project @freelance:
	- [ ] write readme.md
		- is this me talking out loud or should I publish this text
	- [ ] another task @due(2017-05-15)

Alas with notes, sometimes useful is having url to files in your computer: emails, pdfs, etc. Taskpaper ideally handle it, but if often crashed with me.

At first I was really thrilled by Taskpaper’s indentation usage, as a way to create sections and sub-subsection within a project. I think they are still useful, but also I found use them sometime too much, which caused having a lack of hierarchy.

I think they might/can be used still, together with `#-###` to delineate project section (this has to be evaluated tbh).

In regard to this, I want to be able to create a new file.todo for each project, *and* being able to parse and filter through them all without problems: this is not currently possible in Takspaper.app. I wonder if it is because on a technical level, having to parse, filter, compare and write on multiple files at the same time is difficult and problematic, or else.

I like the idea of keeping a folder with all the `.todo` files, as well as keeping some of them in other places, like a project folder (if for some reasons there’s how I want to have it).

A first though was to make a smart folder and grab them all based on their file extension. Open the ones I need, use them, etc.

I am now a bit more prone to keep them in one folder, and not have to worry too much.

The main problem with keeping data in multiple files is that it’s more difficult to parse and compare it: what if you want to check what you have to do for next Monday?

That’s why my first idea was to build a little parser able to compare from different files. Probably in python as in am learning it and it seems to be really good at this.

Then I thought having a CLI is not enough for me. I want to have an actual GUI app.

As said, Taskpaper feels to text-based, like, as if I am inside a text window. Which is the case. Drag and drop is flimsy, press a key and you mess up by accident, etc. It’s good for when you are jotting down a bunch of stuff, not great when you are in review mode and want to move thing around.

dot-todo could be indeed a webapp, maybe I am going to learn node.js a bit by doing the classic todo-app, only it’s a bit more elaborated than that.

The reasons to make an (web)app:
1. proper drag and drop and tasks reordering
2. converting dates, and possibly other values, to other formats on the fly
3. a blend of having a quick entry box that is a text box, where you manipulate raw data and quickly transform it in proper syntax, and a viewer to move things around, delete, complete, edit, etc. Imaging dumping a long list of stuff to do from an email into the app, convert the list to be a task-list with either a button or a shortcut (eventually add tags etc), and press enter. Then going through each or more tasks at once and drag them to appropriate project, or select some of them and assign a due date. 
4. views, or filters, or saved searches: this should be easily configurable with a config file: this file should translate also in ‘panel’ version to toggle things on and off. At the same time, the config file can be easily accessed by any text editor and edited through another app.
5. finally, the app should be able to fire due reminders, using the OS native system when possible (I just know that’s the only useful Notification I found in macOS). I personally like more when my phone displays a reminder for something, and I wonder if a todo app should display reminders at all, as I mostly associate them with calendar events, but this could be an option.

The app should still maintain the power, speed, and flexibility of manipulating raw text, with the ability to transform each task into an ‘atom’, something you can interact with, modify etc. without feeling you are still in a text box.

* * *

Make a python script that:
1. parse all the files in that folder
2. create and or update a today.todo containing all tasks either tagged with @today or with @due(date-of-today)
3. create and or update a week.todo containing all tasks tagged with a @due(date-of-today) that’s within the coming seven days
4. if tasks are due yesterday, leave them in today.todo and week.todo under `## overtime`
