label Y1_S3_C1:
    $ curchpt = 3
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False
    $ didwhatnext = False

    scene office

    "A few days later, you get an email from your advisor to meet in their office..."
    show advisorTalk
    d "Hi [name], I'm your advisor, [d]!"
    hide advisorTalk
    show advisor
    p "It's nice to meet you!"
    hide advisor
    show advisorTalk
    d "Likewise! I just wanted to meet with you real fast to go over my role as your advisor."
    d "I will be here to, well, advise you! I am available to give you advice and direction in a lot of areas."
    d "I will also be checking in now and then, along with keeping an eye on you to make sure you are doing well in school."
    hide advisorTalk
    show advisorSmile
    d "If you ever have any questions, feel free to reach out."
    p "Sounds great! Thank you and I'll see you later!"
    hide advisorSmile
    hide advisor
    hide advisorTalk
    jump Y1_S3_C1_1


label Y1_S3_C1_1:
    scene careerfair
    "Some time has passed, and you heard that Career Services was hosting a fair today so you decide to check it out."
    "It looks really cool! There are a ton of companies here that at first it seems overwhelming, but then one in particular catches your eye."
    "Just as you are about to make your way there, someone walks up to you..."
    show bobTalk at left with dissolve
    $ lefts = False
    b "Welcome to the Career and Internship Fair!"
    b "Feel free to walk around and look at the organizations here. We are also going to have a presentation on professionalism if you are interested!"
    hide bobTalk
    show bob at left
    "You were interested in the company, but maybe the presentation won't be so scary?"
    menu:
        "What would you like to do?"
        "Visit booth":
            jump Y1_S3_C2
        "Go to presentation":
            jump Y1_S3_C3


label Y1_S3_C2:
    p "I think I am going to see what's around first."

    show bobTalk at left
    b "Sounds good, I'm going to go to the presentation."
    hide bobTalk
    hide bob with dissolve

    "You walk around and see what the fair has to offer at first. It seems to have some pretty cool companies but you are only interested in one."

    "Company X."

    "{i}This has everything I hoped for out of a job... I can't believe they are looking for someone here!{/i}"

    "You walk up to their booth."

    show compx with dissolve

    p "Uh, hi there, are you still looking to hire someone?"

    show compxTalk
    x "Yes! We are looking to hire graduates for full-time positions and undergraduates for internship programs. Are you interested?"
    hide compxTalk

    p "Very! What do I need to do to apply?"

    show compxTalk
    x "Well I see you have a resume in hand, do you mind if I look over it real fast?"
    hide compxTalk

    p "Have at it!"

    "You hand her the resume. She spends a minute reading over it before handing it back"

    show compxTalk
    x "You've done some great work so far, but I'm afraid our company is looking for applicants with a little more experience."
    hide compxTalk

    p "I understand, is there anything I can specifically do to help me out?"

    "She points to a big sign in the room that says 'Career Competencies'"

    show compxTalk
    x "Those eight concepts are very important to our business. Once you get a good understanding of them and gain a bit more experience, we would love to have you on the team."

    x "I would recommend talking to Career Services. They put this fair together and can help tremendously. I believe you can find them in the SLTC."
    hide compxTalk

    p "Okay, thank you for your time!"
    hide compx with dissolve



    "A little disappointed but filled with motivation, you decide to work hard to reach your goal of working with that team."
    $ allowed = allowed + 2
    $ dev += 30
    $ professional += 10
    $ communication += 10
    hide bob with dissolve
    call exhausted from _call_exhausted
    call resume from _call_resume_5
    call hdxtoday from _call_hdxtoday_5
    call map from _call_map_5

    jump Y2_S1_C0


label Y1_S3_C3:
    p "I think I'll go to the presentation."

    show bobTalk at left
    b "Mind if I join? I planned on doing the same thing."
    hide bobTalk

    "Bob walks with you to the talk, also interested in what there is to learn"

    show bobTalk at left
    b "So, is this your first time at the Career and Internship Fair, [name]?"
    hide bobTalk

    p "Yeah it is, I'm just a freshman so this is my first one."

    show bobTalk at left
    b "Hey way to get started early! I wish I had started coming to these my freshman year. I had no idea you could learn so much from them."
    hide bobTalk

    p "I'm excited. This should be fun!"

    hide bob
    scene careerfairtalk

    "You both enter the room and take a seat. Someone walks on stage and begins to talk about personal accountability."

    "The talk develops and you become captivated by what the speaker is saying. You learn a lot throughout this talk and walk out feeling a higher sense of responsibility."



    show bobTalk at left with dissolve

    b "That was great! I didn't expect to get that much out of it."
    hide bobTalk
    show bob at left

    p "No me neither, I'm glad we did this!"

    "You walk around the career fair a bit more, but things are winding down and you decide to call it a day."
    $ allowed = allowed + 2
    $ dev += 10
    $ professional += 35
    $ communication += 5
    $ thinking += 5
    hide bob with dissolve
    call exhausted from _call_exhausted_1
    call resume from _call_resume_6
    call hdxtoday from _call_hdxtoday_6
    call map from _call_map_6
    jump Y2_S1_C0

label Y1_S3_C4:
    b "I agree!"
    call exhausted from _call_exhausted_2
    call resume from _call_resume_7
    call map from _call_map_7
    jump Y2_S1_C0
