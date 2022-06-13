from flaskr.model import Achievements, Children_Missions_Association, db,Missions,Lessons_Content,Users,Usages,Avatars,Children,Badges,Lessons,Missions
from flaskr.model import Multiple_choices,Short_answers,Arrange_sentences,Materials,Quizzes,Questions_Class
from flaskr.model import Children_Achievements_Association, Children_Badges_Association, Scores_Association, Progress
from flaskr.model import Material_Content_Class, Multiple_Choices_Answers_Class, Arrange_Sentences_Answer_Choices_Class
db.drop_all()
db.create_all()
# Multiple_choices_answers, Arrange_sentences_answer_choices

avatar1 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarF1.jpg") 
avatar2 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarF2.jpg") 
avatar3 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarF3.jpg") 
avatar4 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarF4.jpg") 
avatar5 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarF5.jpg") 
avatar6 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarM1.jpg") 
avatar7 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarM2.jpg") 
avatar8 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarM3.jpg") 
avatar9 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarM4.jpg") 
avatar10 = Avatars(image_url="https://storage.cloud.google.com/tardigrade-bucket/avatar-img/avatarM5.jpg") 

db.session.add_all([avatar1,avatar2,avatar3,avatar4,avatar5,avatar6,avatar7,avatar8,avatar9,avatar10])

user1 = Users(email="user1@gmail.com", password="123456", name="deka", pin="123123", avatar_users=avatar1) 
user2 = Users(email="user2@gmail.com", password="123456", name="deka", pin="222222", avatar_users=avatar2) 
user3 = Users(email="user3@gmail.com", password="123456", name="deka", pin="333333", avatar_users=avatar3) 
user4 = Users(email="user4@gmail.com", password="123456", name="deka", pin="444444", avatar_users=avatar1) 
user5 = Users(email="user5@gmail.com", password="123456", name="deka", pin="555555", avatar_users=avatar2) 
user6 = Users(email="user6@gmail.com", password="123456", name="deka", pin="666666", avatar_users=avatar3) 

db.session.add_all([user1,user2,user3,user4,user5,user6])

children1 = Children(name="children1", level=1, users_children=user1, avatar_children=avatar1)
children2 = Children(name="children2", level=2, users_children=user2, avatar_children=avatar2)
children3 = Children(name="children3", level=3, users_children=user3, avatar_children=avatar3)
children4 = Children(name="children4", level=4, users_children=user4, avatar_children=avatar1)
children5 = Children(name="children5", level=5, users_children=user5, avatar_children=avatar2)
children6 = Children(name="children6", level=6, users_children=user6, avatar_children=avatar3)
children7 = Children(name="children7", level=7, users_children=user1, avatar_children=avatar1)
children8 = Children(name="children8", level=8, users_children=user2, avatar_children=avatar2)
children9 = Children(name="children9", level=9, users_children=user3, avatar_children=avatar3)
children10 = Children(name="children7", level=10, users_children=user4, avatar_children=avatar1)
children11 = Children(name="children8", level=11, users_children=user5, avatar_children=avatar2)
children12 = Children(name="children9", level=12, users_children=user6, avatar_children=avatar3)

db.session.add_all([children1,children2,children3,children4,children5,children6,children7,children8,children9,children10,children11,children12])

usages1 = Usages(children=children1)
usages2 = Usages(children=children2)
usages3 = Usages(children=children3)
usages4 = Usages(children=children4)
usages5 = Usages(children=children1)
usages6 = Usages(children=children2)
usages7 = Usages(children=children3)
usages8 = Usages(children=children4)
usages9 = Usages(children=children1)

db.session.add_all([usages1, usages2, usages3, usages4, usages5, usages6, usages7, usages8, usages9])

badges0 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/placement-test.png")
badges1 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/alphabets.png")
badges2 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/animals.png")
badges3 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/family.png")
badges4 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/colors.png")
badges5 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/body-parts.png")
badges6 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/greetings.png")
badges7 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/intro-self.png")
badges8 = Badges(image_url="https://storage.cloud.google.com/tardigrade-bucket/badge-img/intro-others.png")

db.session.add_all([badges0, badges1, badges2, badges3, badges4, badges5, badges6, badges7, badges8])


achievements1 = Achievements(name="achievements 1", image_url="https://storage.cloud.google.com/tardigrade-bucket/achievement-img/a1.png", description="Ini adalah achievement pertamamu")
achievements2 = Achievements(name="achievements 2", image_url="https://storage.cloud.google.com/tardigrade-bucket/achievement-img/a2.png", description="Ini adalah achievement keduamu")
achievements3 = Achievements(name="achievements 3", image_url="https://storage.cloud.google.com/tardigrade-bucket/achievement-img/a3.png", description="Ini adalah achievement ketigamu")

db.session.add_all([achievements1, achievements2, achievements3])

children_achievement1 = Children_Achievements_Association(achievements=achievements1, children=children1)
children_achievement2 = Children_Achievements_Association(achievements=achievements2, children=children1)
children_achievement3 = Children_Achievements_Association(achievements=achievements3, children=children1)
children_achievement4 = Children_Achievements_Association(achievements=achievements1, children=children2)
children_achievement5 = Children_Achievements_Association(achievements=achievements2, children=children2)
children_achievement6 = Children_Achievements_Association(achievements=achievements3, children=children2)
children_achievement7 = Children_Achievements_Association(achievements=achievements1, children=children3)
children_achievement8 = Children_Achievements_Association(achievements=achievements2, children=children3)
children_achievement9 = Children_Achievements_Association(achievements=achievements1, children=children4)

db.session.add_all([children_achievement1, children_achievement2, children_achievement3, children_achievement4, children_achievement5, children_achievement6, children_achievement7, children_achievement8, children_achievement9])

lessons0 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/placement-test.png", level=0, title="Placement Test", type="Placement Test", badges=badges0)
lessons1 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/vocabulary/alphabets.png", level=1, title="Alphabets", type="Vocabulary", badges=badges1)
lessons2 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/vocabulary/animals.png", level=1, title="Animals", type="Vocabulary", badges=badges2)
lessons3 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/vocabulary/family.png", level=1, title="Family", type="Vocabulary", badges=badges3)
lessons4 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/vocabulary/colors.png", level=1, title="Colors", type="Vocabulary", badges=badges4)
lessons5 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/vocabulary/body-parts.png", level=1, title="Body Parts", type="Vocabulary", badges=badges5)
lessons6 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/grammar/intro-self.png", level=1, title="Self Introduction", type="Grammar", badges=badges6)
lessons7 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/grammar/intro-others.png", level=1, title="Introducing Others", type="Grammar", badges=badges7)
lessons8 = Lessons(cover_image="https://storage.cloud.google.com/tardigrade-bucket/cover-img/grammar/greetings.png", level=1, title="Greetings", type="Grammar", badges=badges8)

db.session.add_all([lessons0, lessons1, lessons2, lessons3, lessons4, lessons5, lessons6, lessons7, lessons8])

progress1 = Progress(progress=1, children=children1, lessons=lessons1)
progress2 = Progress(progress=2, children=children1, lessons=lessons2)
progress3 = Progress(progress=3, children=children1, lessons=lessons3)
progress4 = Progress(progress=4, children=children1, lessons=lessons4)
progress5 = Progress(progress=5, children=children1, lessons=lessons5)
progress6 = Progress(progress=6, children=children1, lessons=lessons6)
progress7 = Progress(progress=7, children=children2, lessons=lessons1)
progress8 = Progress(progress=8, children=children3, lessons=lessons1)
progress9 = Progress(progress=9, children=children4, lessons=lessons1)
progress10 = Progress(progress=10, children=children2, lessons=lessons2)
progress11 = Progress(progress=11, children=children3, lessons=lessons2)
progress12 = Progress(progress=12, children=children5, lessons=lessons1)

db.session.add_all([progress1, progress2, progress3, progress4, progress5, progress6, progress7, progress8, progress9, progress10, progress11, progress12])

missions1 = Missions(title="Ini adalah mission 1", type=1, c_duration=10, c_min_score=10, lessons=lessons1)
missions2 = Missions(title="Ini adalah mission 2", type=2, c_duration=20, c_min_score=20, lessons=lessons2)
missions3 = Missions(title="Ini adalah mission 3", type=3, c_duration=30, c_min_score=30, lessons=lessons1)
missions4 = Missions(title="Ini adalah mission 4", type=4, c_duration=40, c_min_score=40, lessons=lessons2)
missions5 = Missions(title="Ini adalah mission 5", type=5, c_duration=50, c_min_score=50, lessons=lessons3)
missions6 = Missions(title="Ini adalah mission 6", type=6, c_duration=10, c_min_score=10, lessons=lessons4)
missions7 = Missions(title="Ini adalah mission 7", type=7, c_duration=20, c_min_score=20, lessons=lessons3)
missions8 = Missions(title="Ini adalah mission 8", type=8, c_duration=30, c_min_score=30, lessons=lessons5)
missions9 = Missions(title="Ini adalah mission 9", type=9, c_duration=40, c_min_score=40, lessons=lessons6)
missions10 = Missions(title="Ini adalah mission 10", type=10, c_duration=50, c_min_score=50, lessons=lessons5)

db.session.add_all([missions1, missions2, missions3, missions4, missions5, missions6, missions7, missions8, missions9, missions10])

children_missions1 = Children_Missions_Association(status=1, missions=missions1, children=children1)
children_missions2 = Children_Missions_Association(status=0, missions=missions2, children=children1)
children_missions3 = Children_Missions_Association(status=1, missions=missions3, children=children1)
children_missions4 = Children_Missions_Association(status=0, missions=missions1, children=children2)
children_missions5 = Children_Missions_Association(status=1, missions=missions2, children=children2)
children_missions6 = Children_Missions_Association(status=1, missions=missions3, children=children2)
children_missions7 = Children_Missions_Association(status=1, missions=missions1, children=children3)
children_missions8 = Children_Missions_Association(status=0, missions=missions2, children=children3)
children_missions9 = Children_Missions_Association(status=1, missions=missions1, children=children4)

db.session.add_all([children_missions1, children_missions2, children_missions3, children_missions4, children_missions5, children_missions6, children_missions7, children_missions8, children_missions9])

children_badges1 = Children_Badges_Association(badges=badges1, children=children1)
children_badges2 = Children_Badges_Association(badges=badges2, children=children1)
children_badges3 = Children_Badges_Association(badges=badges3, children=children1)
children_badges4 = Children_Badges_Association(badges=badges1, children=children2)
children_badges5 = Children_Badges_Association(badges=badges2, children=children2)
children_badges6 = Children_Badges_Association(badges=badges3, children=children2)
children_badges7 = Children_Badges_Association(badges=badges1, children=children3)
children_badges8 = Children_Badges_Association(badges=badges2, children=children3)
children_badges9 = Children_Badges_Association(badges=badges1, children=children4)

db.session.add_all([children_badges1, children_badges2, children_badges3, children_badges4, children_badges5, children_badges6, children_badges7, children_badges8, children_badges9])


materials1 = Materials()
materials2 = Materials()
materials3 = Materials()
materials4 = Materials()
materials5 = Materials()
materials6 = Materials()
materials7 = Materials()
materials8 = Materials()
materials9 = Materials()
materials10 = Materials()

db.session.add_all([materials1, materials2, materials3, materials4, materials5, materials6, materials7, materials8, materials9, materials10])

# PLACEMENT TEST multiple choices
multiple_choices01 = Multiple_choices(q_text="Which one is an animal?", answer="B")
multiple_choices02 = Multiple_choices(q_text="Which animal can fly?", answer="D")
multiple_choices03 = Multiple_choices(q_text="Which word ended with letter e?", answer="B")
multiple_choices04 = Multiple_choices(q_text="Which word is not ended with letter t?", answer="D")
multiple_choices05 = Multiple_choices(q_text="Which family member is the oldest?", answer="C")
multiple_choices06 = Multiple_choices(q_text="Blue + yellow = ?", answer="D")
multiple_choices07 = Multiple_choices(q_text="What part of the body we use to speak?", answer="A")
multiple_choices08 = Multiple_choices(q_text="What do you call a female sibling?", answer="B")
multiple_choices09 = Multiple_choices(q_text="Which animal can be a pet?", answer="C")

db.session.add_all([multiple_choices01, multiple_choices02, multiple_choices03, multiple_choices04, multiple_choices05, multiple_choices06, multiple_choices07, multiple_choices08, multiple_choices09])

# QUIZZES multiple choices
multiple_choices1 = Multiple_choices(q_text="Kata apa yang berawalan huruf a?", answer="C")
multiple_choices2 = Multiple_choices(q_text="Which one says “frog”?", answer="A")
multiple_choices3 = Multiple_choices(q_text="Which family member did you hear?", q_audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/family/mother.wav", answer="A")
multiple_choices4 = Multiple_choices(q_text="What color did you hear?", q_audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/red.wav", answer="C")
multiple_choices5 = Multiple_choices(q_text="What part of the body did you hear?", q_audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/body-parts/hand.wav", answer="D")

db.session.add_all([multiple_choices1, multiple_choices2, multiple_choices3, multiple_choices4, multiple_choices5])

# QUIZZES arrange sentences
arrange_sentences1 = Arrange_sentences(q_text="Hewan apa yang berawalan huruf e dalam Bahasa Inggris?", answer="ele phant")
arrange_sentences2 = Arrange_sentences(q_text="Apa Bahasa Inggris dari kelinci?", answer="rab bit")
arrange_sentences3 = Arrange_sentences(q_text="Apa Bahasa Inggris dari ayah?", answer="fa ther")
arrange_sentences4 = Arrange_sentences(q_text="Apa Bahasa Inggris dari warna ungu?", answer="pur ple")
arrange_sentences5 = Arrange_sentences(q_text="Apa Bahasa Inggris dari kaki?", answer="fo ot")

db.session.add_all([arrange_sentences1, arrange_sentences2, arrange_sentences3, arrange_sentences4, arrange_sentences5])

# QUIZZES short answer
short_answer1 = Short_answers(type="image", q_text="elephant", answer="elephant")
short_answer2 = Short_answers(type="audio", q_text="d", answer="d")
short_answer3 = Short_answers(type="image", q_text="butterfly", answer="butterfly")
short_answer4 = Short_answers(type="audio", q_text="rabbit", answer="rabbit")
short_answer5 = Short_answers(type="image", q_text="father", answer="father")
short_answer6 = Short_answers(type="audio", q_text="mother", answer="mother")
short_answer7 = Short_answers(type="image", q_text="purple", answer="purple")
short_answer8 = Short_answers(type="audio", q_text="orange", answer="orange")
short_answer9 = Short_answers(type="image", q_text="knee", answer="knee")
short_answer10 = Short_answers(type="audio", q_text="hand", answer="hand")

db.session.add_all([short_answer1, short_answer2, short_answer3, short_answer4, short_answer5, short_answer6, short_answer7, short_answer8, short_answer9, short_answer10])

quizzes0 = Quizzes(is_final=False)
quizzes1 = Quizzes(is_final=False)
quizzes2 = Quizzes(is_final=False)
quizzes3 = Quizzes(is_final=False)
quizzes4 = Quizzes(is_final=False)
quizzes5 = Quizzes(is_final=False)

db.session.add_all([quizzes1, quizzes2, quizzes3, quizzes4, quizzes5])

score1 = Scores_Association(score=10, quizzes=quizzes1, progress=progress1)
score2 = Scores_Association(score=10, quizzes=quizzes1, progress=progress2)
score3 = Scores_Association(score=10, quizzes=quizzes1, progress=progress3)
score4 = Scores_Association(score=10, quizzes=quizzes2, progress=progress1)
score5 = Scores_Association(score=10, quizzes=quizzes2, progress=progress2)
score6 = Scores_Association(score=10, quizzes=quizzes2, progress=progress3)

db.session.add_all([score1, score2, score3, score4, score5, score6])

lessons_content0 = Lessons_Content(order=1, type=0, title="Placement Test", lessons=lessons0, quizzes=quizzes0)
lessons_content1 = Lessons_Content(order=2, type=1, title="Alphabets A-E", lessons=lessons1, materials=materials1)
lessons_content2 = Lessons_Content(order=3, type=2, title="Latihan Alphabets A-E", lessons=lessons1, quizzes=quizzes1)
lessons_content3 = Lessons_Content(order=4, type=1, title="Small Animals", lessons=lessons2, materials=materials2)
lessons_content4 = Lessons_Content(order=5, type=1, title="Latihan Small Animals", lessons=lessons2, quizzes=quizzes2)
lessons_content5 = Lessons_Content(order=6, type=1, title="Family", lessons=lessons3, materials=materials3)
lessons_content6 = Lessons_Content(order=7, type=1, title="Latihan Family", lessons=lessons3, quizzes=quizzes3)
lessons_content7 = Lessons_Content(order=8, type=1, title="Prime and Secondary Colors", lessons=lessons4, materials=materials4)
lessons_content8 = Lessons_Content(order=9, type=1, title="Latihan Prime and Secondary Colors", lessons=lessons4, quizzes=quizzes4)
lessons_content9 = Lessons_Content(order=10, type=1, title="Parts of Body", lessons=lessons5, materials=materials5)
lessons_content10 = Lessons_Content(order=11, type=1, title="Latihan Parts of Body", lessons=lessons5, quizzes=quizzes5)

db.session.add_all([lessons_content0])
db.session.add_all([lessons_content1, lessons_content2, lessons_content3, lessons_content4, lessons_content5])
db.session.add_all([lessons_content6, lessons_content7, lessons_content8, lessons_content9, lessons_content10])


# ALPHABETS
material_content1 = Material_Content_Class(order=1, text="A for apple", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/alphabets/a-apple.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/alphabets/a-apple.wav", materials=materials1)
material_content2 = Material_Content_Class(order=2, text="B for boat", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/alphabets/b-boat.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/alphabets/b-boat.wav", materials=materials1)
material_content3 = Material_Content_Class(order=3, text="C for car", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/alphabets/c-car.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/alphabets/c-car.wav", materials=materials1)
material_content4 = Material_Content_Class(order=4, text="D for dog", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/alphabets/d-dog.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/alphabets/d-dog.wav", materials=materials1)
material_content5 = Material_Content_Class(order=5, text="E for elephant", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/alphabets/e-elephant.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/alphabets/e-elephant.wav", materials=materials1)

# ANIMALS
material_content6 = Material_Content_Class(order=1, text="Ant", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/animals/ant.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/ant.wav", materials=materials2)
material_content7 = Material_Content_Class(order=2, text="Butterfly", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/animals/butterfly.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/butterfly.wav", materials=materials2)
material_content8 = Material_Content_Class(order=3, text="Frog", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/animals/frog.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/frog.wav", materials=materials2)
material_content9 = Material_Content_Class(order=4, text="Mouse", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/animals/mouse.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/mouse.wav", materials=materials2)
material_content10 = Material_Content_Class(order=5, text="Rabbit", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/animals/rabbit.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/rabbit.wav", materials=materials2)

# FAMILY
material_content11 = Material_Content_Class(order=1, text="Father", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/family/father.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/family/father.wav", materials=materials3)
material_content12 = Material_Content_Class(order=2, text="Mother", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/family/mother.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/family/mother.wav", materials=materials3)

# COLORS
material_content13 = Material_Content_Class(order=1, text="Red", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/colors/red.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/red.wav", materials=materials4)
material_content14 = Material_Content_Class(order=2, text="Yellow", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/colors/yellow.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/yellow.wav", materials=materials4)
material_content15 = Material_Content_Class(order=3, text="Blue", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/colors/blue.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/blue.wav", materials=materials4)
material_content16 = Material_Content_Class(order=4, text="Orange", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/colors/orange.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/orange.wav", materials=materials4)
material_content17 = Material_Content_Class(order=5, text="Green", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/colors/green.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/green.wav", materials=materials4)
material_content18 = Material_Content_Class(order=6, text="Purple", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/colors/purple.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/purple.wav", materials=materials4)

# PART OF BODY
material_content19 = Material_Content_Class(order=1, text="Head", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/body-parts/head.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/body-parts/head.wav", materials=materials5)
material_content20 = Material_Content_Class(order=2, text="Hand", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/body-parts/hand.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/body-parts/hand.wav", materials=materials5)
material_content21 = Material_Content_Class(order=3, text="Knee", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/body-parts/knee.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/body-parts/knee.wav", materials=materials5)
material_content22 = Material_Content_Class(order=4, text="Foot", image="https://storage.cloud.google.com/tardigrade-bucket/lesson-img/body-parts/foot.jpg", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/body-parts/foot.wav", materials=materials5)

db.session.add_all([material_content1, material_content2, material_content3, material_content4, material_content5, material_content6, material_content7, material_content8, material_content9, material_content10])
db.session.add_all([material_content11, material_content12, material_content13, material_content14, material_content15, material_content16, material_content17, material_content18, material_content19, material_content20])
db.session.add_all([material_content21, material_content22])


# PLACEMENT TEST questions
questions01 = Questions_Class(order=1, type=0, quizzes=quizzes0, multiple_choices=multiple_choices01)
questions02 = Questions_Class(order=2, type=0, quizzes=quizzes0, multiple_choices=multiple_choices02)
questions03 = Questions_Class(order=3, type=0, quizzes=quizzes0, multiple_choices=multiple_choices03)
questions04 = Questions_Class(order=4, type=0, quizzes=quizzes0, multiple_choices=multiple_choices04)
questions05 = Questions_Class(order=5, type=0, quizzes=quizzes0, multiple_choices=multiple_choices05)
questions06 = Questions_Class(order=6, type=0, quizzes=quizzes0, multiple_choices=multiple_choices06)
questions07 = Questions_Class(order=7, type=0, quizzes=quizzes0, multiple_choices=multiple_choices07)
questions08 = Questions_Class(order=8, type=0, quizzes=quizzes0, multiple_choices=multiple_choices08)
questions09 = Questions_Class(order=9, type=0, quizzes=quizzes0, multiple_choices=multiple_choices09)

db.session.add_all([questions01, questions02, questions03, questions04, questions05, questions06, questions07, questions08, questions09])

# ALPHABETS
questions1 = Questions_Class(order=1, type=0, quizzes=quizzes1, multiple_choices=multiple_choices1)
questions2 = Questions_Class(order=2, type=1, quizzes=quizzes1, short_answers=short_answer1)
questions3 = Questions_Class(order=3, type=1, quizzes=quizzes1, short_answers=short_answer2)
questions4 = Questions_Class(order=4, type=2, quizzes=quizzes1, arrange_sentences=arrange_sentences1)

# ANIMALS
questions5 = Questions_Class(order=1, type=0, quizzes=quizzes2, multiple_choices=multiple_choices2)
questions6 = Questions_Class(order=2, type=1, quizzes=quizzes2, short_answers=short_answer3)
questions7 = Questions_Class(order=3, type=1, quizzes=quizzes2, short_answers=short_answer4)
questions8 = Questions_Class(order=4, type=2, quizzes=quizzes2, arrange_sentences=arrange_sentences2)

# FAMILY
questions9 = Questions_Class(order=1, type=0, quizzes=quizzes3, multiple_choices=multiple_choices3)
questions10 = Questions_Class(order=2, type=1, quizzes=quizzes3, short_answers=short_answer5)
questions11 = Questions_Class(order=3, type=1, quizzes=quizzes3, short_answers=short_answer6)
questions12 = Questions_Class(order=4, type=2, quizzes=quizzes3, arrange_sentences=arrange_sentences3)

# COLORS
questions13 = Questions_Class(order=1, type=0, quizzes=quizzes4, multiple_choices=multiple_choices4)
questions14 = Questions_Class(order=2, type=1, quizzes=quizzes4, short_answers=short_answer7)
questions15 = Questions_Class(order=3, type=1, quizzes=quizzes4, short_answers=short_answer8)
questions16 = Questions_Class(order=4, type=2, quizzes=quizzes4, arrange_sentences=arrange_sentences4)

# PART OF BODY
questions17 = Questions_Class(order=1, type=0, quizzes=quizzes5, multiple_choices=multiple_choices5)
questions18 = Questions_Class(order=2, type=1, quizzes=quizzes5, short_answers=short_answer9)
questions19 = Questions_Class(order=3, type=1, quizzes=quizzes5, short_answers=short_answer10)
questions20 = Questions_Class(order=4, type=2, quizzes=quizzes5, arrange_sentences=arrange_sentences5)

db.session.add_all([questions1, questions2, questions3, questions4, questions5, questions6, questions7, questions8, questions9, questions10])
db.session.add_all([questions11, questions12, questions13, questions14, questions15, questions16, questions17, questions18, questions19, questions20])


# PLACEMENT TEST multiple choice answer
multiple_choices_answer01 = Multiple_Choices_Answers_Class(choice="A", text="apple", multiple_choices=multiple_choices01)
multiple_choices_answer02 = Multiple_Choices_Answers_Class(choice="B", text="rabbit", multiple_choices=multiple_choices01)
multiple_choices_answer03 = Multiple_Choices_Answers_Class(choice="C", text="boat", multiple_choices=multiple_choices01)
multiple_choices_answer04 = Multiple_Choices_Answers_Class(choice="D", text="car", multiple_choices=multiple_choices01)

multiple_choices_answer05 = Multiple_Choices_Answers_Class(choice="A", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/ant.wav", multiple_choices=multiple_choices02)
multiple_choices_answer06 = Multiple_Choices_Answers_Class(choice="B", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/rabbit.wav", multiple_choices=multiple_choices02)
multiple_choices_answer07 = Multiple_Choices_Answers_Class(choice="C", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/frog.wav", multiple_choices=multiple_choices02)
multiple_choices_answer08 = Multiple_Choices_Answers_Class(choice="D", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/butterfly.wav", multiple_choices=multiple_choices02)

multiple_choices_answer09 = Multiple_Choices_Answers_Class(choice="A", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/rabbit.wav", multiple_choices=multiple_choices03)
multiple_choices_answer010 = Multiple_Choices_Answers_Class(choice="B", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/mouse.wav", multiple_choices=multiple_choices03)
multiple_choices_answer011 = Multiple_Choices_Answers_Class(choice="C", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/ant.wav", multiple_choices=multiple_choices03)
multiple_choices_answer012 = Multiple_Choices_Answers_Class(choice="D", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/frog.wav", multiple_choices=multiple_choices03)

multiple_choices_answer013 = Multiple_Choices_Answers_Class(choice="A", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/ant.wav", multiple_choices=multiple_choices04)
multiple_choices_answer014 = Multiple_Choices_Answers_Class(choice="B", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/rabbit.wav", multiple_choices=multiple_choices04)
multiple_choices_answer015 = Multiple_Choices_Answers_Class(choice="C", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/elephant.wav", multiple_choices=multiple_choices04)
multiple_choices_answer016 = Multiple_Choices_Answers_Class(choice="D", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/lion.wav", multiple_choices=multiple_choices04)

multiple_choices_answer017 = Multiple_Choices_Answers_Class(choice="A", text="sister", multiple_choices=multiple_choices05)
multiple_choices_answer018 = Multiple_Choices_Answers_Class(choice="B", text="father", multiple_choices=multiple_choices05)
multiple_choices_answer019 = Multiple_Choices_Answers_Class(choice="C", text="grandmother", multiple_choices=multiple_choices05)
multiple_choices_answer020 = Multiple_Choices_Answers_Class(choice="D", text="mother", multiple_choices=multiple_choices05)

multiple_choices_answer021 = Multiple_Choices_Answers_Class(choice="A", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/purple.wav", multiple_choices=multiple_choices06)
multiple_choices_answer022 = Multiple_Choices_Answers_Class(choice="B", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/orange.wav", multiple_choices=multiple_choices06)
multiple_choices_answer023 = Multiple_Choices_Answers_Class(choice="C", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/red.wav", multiple_choices=multiple_choices06)
multiple_choices_answer024 = Multiple_Choices_Answers_Class(choice="D", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/colors/green.wav", multiple_choices=multiple_choices06)

multiple_choices_answer025 = Multiple_Choices_Answers_Class(choice="A", text="mouth", multiple_choices=multiple_choices07)
multiple_choices_answer026 = Multiple_Choices_Answers_Class(choice="B", text="nose", multiple_choices=multiple_choices07)
multiple_choices_answer027 = Multiple_Choices_Answers_Class(choice="C", text="hand", multiple_choices=multiple_choices07)
multiple_choices_answer028 = Multiple_Choices_Answers_Class(choice="D", text="foot", multiple_choices=multiple_choices07)

multiple_choices_answer029 = Multiple_Choices_Answers_Class(choice="A", text="brother", multiple_choices=multiple_choices08)
multiple_choices_answer030 = Multiple_Choices_Answers_Class(choice="B", text="sister", multiple_choices=multiple_choices08)
multiple_choices_answer031 = Multiple_Choices_Answers_Class(choice="C", text="mother", multiple_choices=multiple_choices08)
multiple_choices_answer032 = Multiple_Choices_Answers_Class(choice="D", text="father", multiple_choices=multiple_choices08)

multiple_choices_answer033 = Multiple_Choices_Answers_Class(choice="A", text="lion", multiple_choices=multiple_choices09)
multiple_choices_answer034 = Multiple_Choices_Answers_Class(choice="B", text="tiger", multiple_choices=multiple_choices09)
multiple_choices_answer035 = Multiple_Choices_Answers_Class(choice="C", text="cat", multiple_choices=multiple_choices09)
multiple_choices_answer036 = Multiple_Choices_Answers_Class(choice="D", text="elephant", multiple_choices=multiple_choices09)

db.session.add_all([multiple_choices_answer01, multiple_choices_answer02, multiple_choices_answer03, multiple_choices_answer04])
db.session.add_all([multiple_choices_answer05, multiple_choices_answer06, multiple_choices_answer07, multiple_choices_answer08])
db.session.add_all([multiple_choices_answer09, multiple_choices_answer010, multiple_choices_answer011, multiple_choices_answer012])
db.session.add_all([multiple_choices_answer013, multiple_choices_answer014, multiple_choices_answer015, multiple_choices_answer016])
db.session.add_all([multiple_choices_answer017, multiple_choices_answer018, multiple_choices_answer019, multiple_choices_answer020])
db.session.add_all([multiple_choices_answer021, multiple_choices_answer022, multiple_choices_answer023, multiple_choices_answer024])
db.session.add_all([multiple_choices_answer025, multiple_choices_answer026, multiple_choices_answer027, multiple_choices_answer028])
db.session.add_all([multiple_choices_answer029, multiple_choices_answer030, multiple_choices_answer031, multiple_choices_answer032])
db.session.add_all([multiple_choices_answer033, multiple_choices_answer034, multiple_choices_answer035, multiple_choices_answer036])


# QUIZZES multiple choice answer
multiple_choices_answer1 = Multiple_Choices_Answers_Class(choice="A", text="dog", multiple_choices=multiple_choices1)
multiple_choices_answer2 = Multiple_Choices_Answers_Class(choice="B", text="boat", multiple_choices=multiple_choices1)
multiple_choices_answer3 = Multiple_Choices_Answers_Class(choice="C", text="apple", multiple_choices=multiple_choices1)
multiple_choices_answer4 = Multiple_Choices_Answers_Class(choice="D", text="elephant", multiple_choices=multiple_choices1)

multiple_choices_answer5 = Multiple_Choices_Answers_Class(choice="A", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/frog.wav", multiple_choices=multiple_choices2)
multiple_choices_answer6 = Multiple_Choices_Answers_Class(choice="B", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/elephant.wav", multiple_choices=multiple_choices2)
multiple_choices_answer7 = Multiple_Choices_Answers_Class(choice="C", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/rabbit.wav", multiple_choices=multiple_choices2)
multiple_choices_answer8 = Multiple_Choices_Answers_Class(choice="D", audio="https://storage.cloud.google.com/tardigrade-bucket/lesson-audio/animals/ant.wav", multiple_choices=multiple_choices2)

multiple_choices_answer9 = Multiple_Choices_Answers_Class(choice="A", text="mother", multiple_choices=multiple_choices3)
multiple_choices_answer10 = Multiple_Choices_Answers_Class(choice="B", text="sister", multiple_choices=multiple_choices3)
multiple_choices_answer11 = Multiple_Choices_Answers_Class(choice="C", text="brother", multiple_choices=multiple_choices3)
multiple_choices_answer12 = Multiple_Choices_Answers_Class(choice="D", text="father", multiple_choices=multiple_choices3)

multiple_choices_answer13 = Multiple_Choices_Answers_Class(choice="A", text="purple", multiple_choices=multiple_choices4)
multiple_choices_answer14 = Multiple_Choices_Answers_Class(choice="B", text="green", multiple_choices=multiple_choices4)
multiple_choices_answer15 = Multiple_Choices_Answers_Class(choice="C", text="red", multiple_choices=multiple_choices4)
multiple_choices_answer16 = Multiple_Choices_Answers_Class(choice="D", text="blue", multiple_choices=multiple_choices4)

multiple_choices_answer17 = Multiple_Choices_Answers_Class(choice="A", text="head", multiple_choices=multiple_choices5)
multiple_choices_answer18 = Multiple_Choices_Answers_Class(choice="B", text="knee", multiple_choices=multiple_choices5)
multiple_choices_answer19 = Multiple_Choices_Answers_Class(choice="C", text="eye", multiple_choices=multiple_choices5)
multiple_choices_answer20 = Multiple_Choices_Answers_Class(choice="D", text="hand", multiple_choices=multiple_choices5)

db.session.add_all([multiple_choices_answer1, multiple_choices_answer2, multiple_choices_answer3, multiple_choices_answer4])
db.session.add_all([multiple_choices_answer5, multiple_choices_answer6, multiple_choices_answer7, multiple_choices_answer8])
db.session.add_all([multiple_choices_answer9, multiple_choices_answer10, multiple_choices_answer11, multiple_choices_answer12])
db.session.add_all([multiple_choices_answer13, multiple_choices_answer14, multiple_choices_answer15, multiple_choices_answer16])
db.session.add_all([multiple_choices_answer17, multiple_choices_answer18, multiple_choices_answer19, multiple_choices_answer20])


# QUIZZES arrange sentences answer choices
arrange_sentences_answer_choices1 = Arrange_Sentences_Answer_Choices_Class(word="ele", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices2 = Arrange_Sentences_Answer_Choices_Class(word="butter", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices3 = Arrange_Sentences_Answer_Choices_Class(word="phant", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices4 = Arrange_Sentences_Answer_Choices_Class(word="fly", arrange_sentences=arrange_sentences1)

arrange_sentences_answer_choices5 = Arrange_Sentences_Answer_Choices_Class(word="fly", arrange_sentences=arrange_sentences2)
arrange_sentences_answer_choices6 = Arrange_Sentences_Answer_Choices_Class(word="rab", arrange_sentences=arrange_sentences2)
arrange_sentences_answer_choices7 = Arrange_Sentences_Answer_Choices_Class(word="butter", arrange_sentences=arrange_sentences2)
arrange_sentences_answer_choices8 = Arrange_Sentences_Answer_Choices_Class(word="bit", arrange_sentences=arrange_sentences2)

arrange_sentences_answer_choices9 = Arrange_Sentences_Answer_Choices_Class(word="grand", arrange_sentences=arrange_sentences3)
arrange_sentences_answer_choices10 = Arrange_Sentences_Answer_Choices_Class(word="ther", arrange_sentences=arrange_sentences3)
arrange_sentences_answer_choices11 = Arrange_Sentences_Answer_Choices_Class(word="mo", arrange_sentences=arrange_sentences3)
arrange_sentences_answer_choices12 = Arrange_Sentences_Answer_Choices_Class(word="fa", arrange_sentences=arrange_sentences3)

arrange_sentences_answer_choices13 = Arrange_Sentences_Answer_Choices_Class(word="yel", arrange_sentences=arrange_sentences4)
arrange_sentences_answer_choices14 = Arrange_Sentences_Answer_Choices_Class(word="ple", arrange_sentences=arrange_sentences4)
arrange_sentences_answer_choices15 = Arrange_Sentences_Answer_Choices_Class(word="pur", arrange_sentences=arrange_sentences4)
arrange_sentences_answer_choices16 = Arrange_Sentences_Answer_Choices_Class(word="low", arrange_sentences=arrange_sentences4)

arrange_sentences_answer_choices17 = Arrange_Sentences_Answer_Choices_Class(word="h", arrange_sentences=arrange_sentences5)
arrange_sentences_answer_choices18 = Arrange_Sentences_Answer_Choices_Class(word="and", arrange_sentences=arrange_sentences5)
arrange_sentences_answer_choices19 = Arrange_Sentences_Answer_Choices_Class(word="fo", arrange_sentences=arrange_sentences5)
arrange_sentences_answer_choices20 = Arrange_Sentences_Answer_Choices_Class(word="ot", arrange_sentences=arrange_sentences5)

db.session.add_all([arrange_sentences_answer_choices1,arrange_sentences_answer_choices2,arrange_sentences_answer_choices3,arrange_sentences_answer_choices4,arrange_sentences_answer_choices5])
db.session.add_all([arrange_sentences_answer_choices6,arrange_sentences_answer_choices7,arrange_sentences_answer_choices8,arrange_sentences_answer_choices9,arrange_sentences_answer_choices10])
db.session.add_all([arrange_sentences_answer_choices11,arrange_sentences_answer_choices12,arrange_sentences_answer_choices13,arrange_sentences_answer_choices14,arrange_sentences_answer_choices15])
db.session.add_all([arrange_sentences_answer_choices16,arrange_sentences_answer_choices17,arrange_sentences_answer_choices18,arrange_sentences_answer_choices19,arrange_sentences_answer_choices20])

db.session.commit()