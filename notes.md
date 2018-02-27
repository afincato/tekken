
## for a critique of plain-text todo: apps, syntaxes, intents, usages

(05-05-2017)

(one of the many notes written between May and August 2017 while playing with the code; written all in one go and never checked it out so pretty messy; plan to review them and put a better text together)

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

## Notes on ideal todo list setup

* each project has its own .md file
* make use of markdown tasklist syntax, instead of making a new line (see `todo.txt`), or a new line with a dash (taskpaper)

* prefer taskpaper syntax over todo.txt’s, so use @tags, @context(example), @due(2017-04-29), etc.
* this syntax is part of the file and not an extra layer managed by that specific app (so not even Open Meta tags stuff)
	* (though on this point, I sometimes began to think which kind of metadata you can add to the simplest file (let’s say a text-file) which you can be sure it will live until that file will exist. So beyond Creation and Modification date, macOS tags are somehow nice, but only working on macOS I imagine)
* I like to tag a text file directly on its title, so then you simply write #tagname on nvALT and all files with that tag appear, but it would also be nice to maybe add these tags as the first line after the title? I guess both approaches work well in nvALT, and in the latter case, are the preferred method by an app like 1Writer (which, though, reads as #tag also bits of a url, that’s not cool—I wrote to the dev last Autumn about it and never heard back (that’s fine) but then tried to use iaWriter for my notes on phone and did not know if they fixed that problem)
* Then, should tags be #tag, and @ used for @due(2017-04-29), @context(af), etc? # do not work on Taskpaper, but anyway.

* as there are currently no app doing all this (or if it is, it’s a more general note-taking, calendar AND todo list app), try to stick with nvALT again, this means:
	* deadline with @due() cannot be easily setup (but first try [nvmind](http://brettterpstra.com/projects/nvremind/) script that triggers an macOS notificaton——the only reason why notifications can be useful, imo, are because of event-based reminders)
	* nvALT is great for filtering, and since each project has its own file, it becomes maybe easier than having to setup custom searches like in Taskpaper? But then, there are cases you want to filter through `due today` or `due this week` tasks, and am not sure how to do that in nvALT (without a script and without having to constantly editing tasks)
	* these two points would ideally push me to use more a Calendar for deadline and stuff, but then I am duplicating my input of information
	* I thought than finding an iOS app with due reminders and notifications capabilities would be a way: currently trying SwiftoDo, which seems to have this capabilities; same for Taskmator: ideally it would be great and make more sense to check these things on my phone, but Taskmator is still simply unusable (in this case, the UI is really badly thought out that it’s impractical)
	* to back up the above points: I came to realise I need and want an app also on my phone to add, review and be notified about task-related things. Only using Draft to send to Dropbox (ahem [^1]) a new task to a general inbox.todo is pretty useless—I prefer to simply keep a text file on my phone where to quickly jot down todos and then review them once I am on my laptop)
	* org-mode seem alluring but why learning a new syntax (though no biggie if it works amazingly well), and why having to fire up emacs only for it, and what about system notifications (there might be a package that does that probably), but most importantly, there’s not decent (not even great) phone app. Also, mixing todos and notes sounds amazing but confusing as well. I like to keep notes all over the place, ideally if I am working on something that needs notes, I want to keep that file in the project folder, and then having possibly a `/notes` folder with all the rest (am still not sure about this dissemination approach tbh, it only came to mind when I began to work more on website stuff and keeping a readme.md was a novelty and I enjoyed it, to the point that sometimes I was keeping a notes.md, set it to be ignored by git, and kept using it——alas for other projects, having a notes.md in that folder sounds better to me, though to quickly search that file I cannot look it up by using nvALT)
	*  there’s no more things to add: major problems in general with text-based todo list is reminders and such, but it’s also true you can use scripts that fire system events, on your laptop at least, so it’s a matter of dedication
	
[^1]: Dropbox: I moved away from it—at least I tried once more, but with a lot of ‘downsides’, mostly keep in sync notes and todos between laptop and phone: I tried to go with iCloud, as iaWriter supports it much more than Dropbox, but iCloud is not like Dropbox: when you put your files in it, it moves your files from Desktop to its servers, unlike with Dropbox that keeps a local copy of all the files on your computer. I don’t want that. No matter the reliability of iCloud, I want to have a copy of my files on my computer, and mirror them to another device through the server, not the other way around. Tried to use Bittorent, but not well integrated with phone apps, played a couple of times with ownCloud, but on my shared hosting plan it was reporting some installation errors or missing modules, though I could access it.

To the point that I began to think: do I really need all my notes on my phone always in sync? Well, maybe my notes not, but my todos yes. Also my notes. I am trying to only use Drafts on phone to jot down text of any sort, and then review it once I am on my laptop, but not working so well. Drafts shines because you can jot down any text and then send it somewhere else, it’s not really design to become an archive (even if a short-term one). Maybe it is, just that when I need that note then, if I don’t use Dropbox, the two other options that come to mind are: iCloud (eeeh), or email (somehow even worse).

So, well. Maybe I should just give up again and use Dropbox for my notes, even though they are pretty sensitive at times, and hoping their newly encrypted measures are actually doing something.

A nice thing would be if iOS, or even Android, would start to use more p2p sync, with certified devices on each end. This on a system level, so any app can access it by default. Then, whenever your devices are connected to the internet, they have a push/fetching mechanism, which you can eventually bypass by doing pull-to-refresh (ofc if this is not required it would be better, but sometimes it’s comforting to know that new data is being downloaded by doing pull-to-refresh in the case you are waiting for changes to be retrieved but nothing is happening yet)

## notes 15012018

use `~~`overwrite`~~` syntax to mark a task as cancelled (instead of simply deleting it?).

## todo-forecast.dat

i'm moving towards the idea of putting together a dat-based app running on beaker and built with choo (lol), to interact with my todo list project and my forecast-project management and possibly invoice maker thing.

at the base there is the todo.txt file and the init.yaml file that build the overview of each project. after parsing them into `json`, i'll be able to visualize all that stuff and make run things against it.

the idea of embedding also the invoice maker project using latex would perfectly work as with this new latex self-contained instance called [tectonic](https://tectonic-typesetting.github.io/en-US/) i could just bind the latex make script to a button.
