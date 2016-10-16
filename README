Created for JacobsHack!2016

## Inspiration
This marked my first time to attend a hackathon, and participating with a project is a must in order to get the full experience. My first goal, in order to destinguish jacobshack from simply a "jam", was to try create something that's less of a traditional program and more of a "bodge" - a weird (albeit useful) combination of many things I can think of.

## What it does
With this bodge, I can control my PC remotely through SMS. You can add as many actions as you want with freedom of choosing the syntax too. You can manage your SMS commands and their syntax from the "maps" file (supports pattern matching with regular expressions).

## How I built it
My computer acts as both a client and a server in a way, but I think it'd be more precisely referred to as a server as that's what Twilio calls it. I set up a local HTTP server using Flask on Python, and then I exposed it through a program called ngrok to the internet. Twelio is the main link between SMS messages, as it "forwards" whatever SMS I send to my Twelio compatible number provided by the trial to the url by ngrock to which the local http server is forwarded. 

So I send an SMS from phone -> Twelio Number -> Twelio's web hook (ngrok url) -> local server -> runs commands on pc -> sends reply SMS to phone.  

For security reasons, I made such that it only listens SMS from my phone number, but this can easily be changed in the file "info.init".

## Challenges I ran into
The biggest challenge was coming up with an idea. An alexa skill sounded very straightforward to me, and even though I had planned to work on one, I couldn't due to the fact that I don't have a credit card/paypal/bank account at this time. Same goes for the domain name which I could have used in the  my project, but couldn't proceed with checking out my free items because I couldn't enter my credit card details.

## Accomplishments that I'm proud of
I'm mostly proud of the fact that I managed to turn in some project. At some point, my brain decided to lock itself away from me, and I was just staring at the screen or playing around without making any apparent progress. It was as if there were sounds inside my head chanting some words along the lines "One always regrets what could have done. Remember for next time.". No, this shouldn't be printed on a hackathon's flier while it's running. Come on.

## What I learned
Before today, I didn't even know what Twilio really was. Same with Alexa. Both of which have presented quite the show today (yesterday? in the last 24 hours, whatever). Before I started, I didn't know what exactly I was going to do, but I knew I was going to need to use something like node.js. It's something that's pretty new to me. I had started setting up my environment and playing around with it around lunch time, but a while after, there was this talk by one of our dear organizers on this other python library which I didn't know much about Flask. Following the talk, I dashed back to my place and started playing with it. And well, it's just wonderful. Sorry node.js. 

## What's next for A-SMS Web Hook
There are still a lot of improvements to be made, some of which requires a Pro Twilio account, like  SMS notifications once a job is done (think of when you want to switch off a computer after long hours of crunching work while you're away or something). Other improvements can include jobs with custom SMS responses (e.g: send an SMS to check your laptop's battery or a download's progress, and you get a response with the value). This would be really easy to implement with a little bit of time.
