# ICPC FCAI CU Community

The website for the ICPC FCAI CU community, a competitive programming training group at the Faculty of Computers and Artificial Intelligence, Cairo University. It puts the community's levels, training waves and live sessions in one place, so members can see what is running now, what is coming next, and where they should start.

## The problem

Student communities usually run on chat groups. A session gets announced on WhatsApp, a reminder goes out on Facebook, the materials end up in a Discord channel, and a few weeks later nobody can find any of it. New members have it the hardest. They join, scroll through hundreds of messages, and still don't know whether they are ready for the advanced material or where the beginner track even begins.

Organizers deal with the same mess from the other side. Every new round of training means rewriting the same announcements, answering the same "when is the next session?" question, and keeping several places up to date by hand.

This site is meant to be the one place that stays correct. The chat groups are still there for conversation, but the schedule and the structure live here.

## How it's organized

There are three building blocks, and they are kept deliberately simple.

**Levels** are the tracks. Each level has its own description, color and thumbnail, so a new member can pick one and immediately know where they stand.

**Waves** are time-boxed training periods. A wave has a start and an end date, and the sessions inside it make up that period's schedule. The home page always shows the current wave.

**Sessions** are the live meetings themselves. Each one belongs to a wave and a level, has a start and end time, a short description, and longer content for notes or materials. The home page surfaces the next upcoming session.

The levels also carry the community's identity. Level 0 is blue (#2b6aad), Level 1 is red (#ad281c) and Level 2 is yellow (#f7ab2f), the same three colors as the logo, and they show up on cards, badges and thumbnails across the site.

## What it does

- A home page with the current wave, the next session and the three levels
- Pages for browsing all levels, waves and sessions, plus the sessions of any single level or wave
- A stable, readable URL for every level, wave and session, so links can be shared in chats without breaking
- Link previews that use each item's own thumbnail when it is shared
- Structured data for search engines (events and courses), canonical URLs and Open Graph tags
- Four themes: light, dark, cream and midnight. The choice is remembered in the browser
- Create, edit and delete pages for staff, without needing the Django admin
- Quick links to the community's channels

## Built with

Django and Tailwind CSS v4, with server-rendered templates and a small amount of vanilla JavaScript. There is no front-end framework on purpose. Pages load fast, search engines can read them without running scripts, and the codebase stays easy for the next batch of members to pick up.

## Status

Early and changing quickly. The public pages are in place, and the management side is still being filled in.

## Contributing

Community members are welcome to help. If you are planning something bigger than a small fix, open an issue first so we can talk it through before you spend time on it.