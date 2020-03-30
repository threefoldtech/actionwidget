# actionwidget
call to action widget

# Flow 

## Normal flow
### Option one: soft (/signup_internet)

 I want an internet

- which allows me to ownf my own data and digital life
- where abuse of my information is not tolerated
-  without the need to burn crazy amounts of fossil fuel to provide my digital life
- where everyone has equal chances
- where I can trust my country to protect my safety and rights
- which is available everywhere in the world at a cost lower than today
- Supported by a token that has real value and represents this new internet (not like dollars trillions will be printed, not like bitcoin no backing)


NEXT->

### Option two strong (/signup_cyborg):


- I acknowledge that I became a cyborg because I cannot live anymore without my smartphone.
- I realize that my cyborg part is not owned by me, I am part of some big AI driven internet cloud.
- I want my digital life back in such a way it's friendly to our planet and my human rights.
- I do not agree that the internet is using up to 10% of the world's electricity and this will become multiple times worse. There needs to be an alternative which is good for the planet.
- I do not agree that the global neutral internet is disappearing, it's being cut in pieces, firewalls are installed everywhere, my data is abused, information is often fake manipulated and there is not much we can do about it, ...


All of this is possible.
ThreeFold has created a new internet solution which allows: ...

NEXT->

### Option three: referred (/signup_referred?userid={userid}):


Text that user has to download the app (3bot connect ).

Button: I have installed the app, continue -> redirect to 3botlogin

Redirect to callback, to signup


### Callback

-> PUT api/referral_done 
{
  "referral_email_address": "referral_email_address",
  "user_id": "user_id_of_referrer",
  "POI": "user_proofofidentity" 
}

### Sign up here section bottom of page (/signup):



- [ ] I want to reserve my digital twin
- [ ] I am interested to have my own video conferencing solution which allows me to communicate with everyone in the world
- [ ] I am interested in a peer2peer alternative social media network for private & business usage
- [ ] I am interested to learn more about become a farmer and provide internet capacity for people around me
- [ ] I am interested to know more about how to deploy my own IT solutions on this new internet (maybe not)

### I agree that…
- [ ] GDPR statement
- [ ] We are allowed to put cookies from our websites
- [ ] We are allowed to email them 

```
if email address is in signup already, dont ask, ask only mobile (user is logged in through 3botconnect)
```

Email address 
Mobile (optional)

-> PUT request 1 to API to save all the data
/api/user/<email_address>
{
 "mobile" : "mobile",
  "reserve_3bot" : true,
  "videoconf" : true,
  "social_media": true,
  "farmer" : true,
  "deploy_it" : true,
  "gdpr: true,
  "cookies": true,
  "email" : true
}

NEXT ->

### 2 last questions (/last):
- [ ] Do you want to refer us to others and be part of our referral program.
- [ ] Are you interested to know more about our related digital currencies?

-> POST request 2 to API to save all the data
/api/set_referral_and_currency
{
    "email_address" : "sameemail"
    "referral" : true,
    "currencies" : true
}


FINISH

## Email Answer 

Email -> depend on checkboxes


### Referral program

Link to frontend (/referral?userid={id}):

#### Page /referral?userid={id}&referrer_token={userreferrer_token}: 

Fill in at least 10 people you want to refer: (Start with 10 input boxes, add more when 10 are full)
...
...
...

Submit
-> PUT /api/referrer
{
  "referrer_token" : "userreferrer_token",
  "referrer_email_address" : "thereferrer@emailaddress.com"
}


### Emails to each person:

You were referred by {person}, please click the link to accept the referral (/signup_referred?userid={userid})
