from flaskr.model import Achievements, Children_Missions_Association, db,Missions,Lessons_Content,Users,Usages,Avatars,Children,Badges,Lessons,Missions
from flaskr.model import Multiple_choices,Short_answers,Arrange_sentences,Materials,Quizzes,Questions_Class
from flaskr.model import Children_Achievements_Association, Children_Badges_Association, Scores_Association, Progress
from flaskr.model import Material_Content_Class, Multiple_Choices_Answers_Class, Arrange_Sentences_Answer_Choices_Class
db.drop_all()
db.create_all()
# Multiple_choices_answers, Arrange_sentences_answer_choices

avatar1 = Avatars(image_url="https://i.pravatar.cc/300?u=1") 
avatar2 = Avatars(image_url="https://i.pravatar.cc/300?u=2") 
avatar3 = Avatars(image_url="https://i.pravatar.cc/300?u=3") 

db.session.add_all([avatar1,avatar2,avatar3])

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

badges1 = Badges(image_url="https://picsum.photos/200")
badges2 = Badges(image_url="https://picsum.photos/200")
badges3 = Badges(image_url="https://picsum.photos/200")
badges4 = Badges(image_url="https://picsum.photos/200")
badges5 = Badges(image_url="https://picsum.photos/200")
badges6 = Badges(image_url="https://picsum.photos/200")

db.session.add_all([badges1, badges2, badges3, badges4, badges5, badges6])


achievements1 = Achievements(name="achievements 1", image_url="https://picsum.photos/200", description="Ini adalah achievement pertamamu")
achievements2 = Achievements(name="achievements 2", image_url="https://picsum.photos/200", description="Ini adalah achievement keduamu")
achievements3 = Achievements(name="achievements 3", image_url="https://picsum.photos/200", description="Ini adalah achievement ketigamu")

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


lessons1 = Lessons(cover_image="https://picsum.photos/200", level=1, title="Pelajaran 1", type="Grammar", badges=badges1)
lessons2 = Lessons(cover_image="https://picsum.photos/200", level=2, title="Pelajaran 2", type="Grammar", badges=badges2)
lessons3 = Lessons(cover_image="https://picsum.photos/200", level=3, title="Pelajaran 3", type="Vocabulary", badges=badges3)
lessons4 = Lessons(cover_image="https://picsum.photos/200", level=4, title="Pelajaran 4", type="Vocabulary", badges=badges4)
lessons5 = Lessons(cover_image="https://picsum.photos/200", level=5, title="Pelajaran 5", type="Grammar", badges=badges5)
lessons6 = Lessons(cover_image="https://picsum.photos/200", level=6, title="Pelajaran 6", type="Grammar", badges=badges6)

db.session.add_all([lessons1, lessons2, lessons3, lessons4, lessons5, lessons6])

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

multiple_choices1 = Multiple_choices(q_text="What is Yol?", q_image="https://picsum.photos/200/300", q_audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", answer="A")
multiple_choices2 = Multiple_choices(q_text="What is Han?", q_image="https://picsum.photos/200/300", q_audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", answer="B")

db.session.add_all([multiple_choices1, multiple_choices2])

arrange_sentences1 = Arrange_sentences(q_text="What is Yol?", q_image="https://picsum.photos/200/300", q_audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", answer="kata11 kata21 kata31")
arrange_sentences2 = Arrange_sentences(q_text="What is Han?", q_image="https://picsum.photos/200/300", q_audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", answer="kata12 kata22 kata32")

db.session.add_all([arrange_sentences1, arrange_sentences2])

short_answer1 = Short_answers(type=0, q_text="What is Yol?", q_image="https://picsum.photos/200/300", q_audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", answer="bed")
short_answer2 = Short_answers(type=1, q_text="What is Han?", q_image="https://picsum.photos/200/300", q_audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", answer="bed")
short_answer3 = Short_answers(type=2, q_text="What is Uf?", q_image="https://picsum.photos/200/300", q_audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", answer="bed")

db.session.add_all([short_answer1, short_answer2, short_answer3])

quizzes1 = Quizzes(is_final=False)
quizzes2 = Quizzes(is_final=True)

db.session.add_all([quizzes1, quizzes2])

score1 = Scores_Association(score=10, quizzes=quizzes1, progress=progress1)
score2 = Scores_Association(score=10, quizzes=quizzes1, progress=progress2)
score3 = Scores_Association(score=10, quizzes=quizzes1, progress=progress3)
score4 = Scores_Association(score=10, quizzes=quizzes2, progress=progress1)
score5 = Scores_Association(score=10, quizzes=quizzes2, progress=progress2)
score6 = Scores_Association(score=10, quizzes=quizzes2, progress=progress3)

db.session.add_all([score1, score2, score3, score4, score5, score6])

lessons_content1 = Lessons_Content(order=1, type=1, title="Materi 1", lessons=lessons1, materials=materials1)
lessons_content2 = Lessons_Content(order=2, type=2, title="Latihan 1", lessons=lessons1, quizzes=quizzes1)
lessons_content3 = Lessons_Content(order=3, type=1, title="Materi 2", lessons=lessons1, materials=materials2)
lessons_content4 = Lessons_Content(order=4, type=2, title="Kuis", lessons=lessons1, quizzes=quizzes2)

db.session.add_all([lessons_content1, lessons_content2, lessons_content3, lessons_content4])

material_content1 = Material_Content_Class(order=1, text="ini adalah material content 1", image="https://picsum.photos/800/360", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", materials=materials1)
material_content2 = Material_Content_Class(order=2, text="ini adalah material content 2", image="https://picsum.photos/800/360", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", materials=materials1)
material_content3 = Material_Content_Class(order=3, text="ini adalah material content 3", image="https://picsum.photos/800/360", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", materials=materials1)
material_content4 = Material_Content_Class(order=1, text="ini adalah material content 1", image="https://picsum.photos/800/360", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", materials=materials2)
material_content5 = Material_Content_Class(order=2, text="ini adalah material content 2", image="https://picsum.photos/800/360", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", materials=materials2)
material_content6 = Material_Content_Class(order=3, text="ini adalah material content 3", image="https://picsum.photos/800/360", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", materials=materials2)

db.session.add_all([material_content1, material_content2, material_content3, material_content4, material_content5, material_content6])

questions1 = Questions_Class(order=1, type=0, quizzes=quizzes1, multiple_choices=multiple_choices1)
questions2 = Questions_Class(order=2, type=1, quizzes=quizzes1, arrange_sentences=arrange_sentences1)
questions3 = Questions_Class(order=3, type=2, quizzes=quizzes1, short_answers=short_answer1)
questions4 = Questions_Class(order=1, type=0, quizzes=quizzes2, multiple_choices=multiple_choices2)
questions5 = Questions_Class(order=2, type=1, quizzes=quizzes2, arrange_sentences=arrange_sentences2)
questions6 = Questions_Class(order=3, type=2, quizzes=quizzes2, short_answers=short_answer2)
questions7 = Questions_Class(order=4, type=2, quizzes=quizzes2, short_answers=short_answer3)

db.session.add_all([questions1, questions2, questions3, questions4, questions5, questions6, questions7])

multiple_choices_answer1 = Multiple_Choices_Answers_Class(choice="A", text="ini adalah multiple choices answer 1", image="https://picsum.photos/300/200", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", multiple_choices=multiple_choices1)
multiple_choices_answer2 = Multiple_Choices_Answers_Class(choice="B", text="ini adalah multiple choices answer 2", image="https://picsum.photos/300/200", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", multiple_choices=multiple_choices1)
multiple_choices_answer3 = Multiple_Choices_Answers_Class(choice="C", text="ini adalah multiple choices answer 3", image="https://picsum.photos/300/200", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", multiple_choices=multiple_choices1)
multiple_choices_answer4 = Multiple_Choices_Answers_Class(choice="D", text="ini adalah multiple choices answer 4", image="https://picsum.photos/300/200", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", multiple_choices=multiple_choices1)
multiple_choices_answer5 = Multiple_Choices_Answers_Class(choice="A", text="ini adalah multiple choices answer 1", image="https://picsum.photos/300/200", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", multiple_choices=multiple_choices2)
multiple_choices_answer6 = Multiple_Choices_Answers_Class(choice="B", text="ini adalah multiple choices answer 2", image="https://picsum.photos/300/200", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", multiple_choices=multiple_choices2)
multiple_choices_answer7 = Multiple_Choices_Answers_Class(choice="C", text="ini adalah multiple choices answer 3", image="https://picsum.photos/300/200", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", multiple_choices=multiple_choices2)
multiple_choices_answer8 = Multiple_Choices_Answers_Class(choice="D", text="ini adalah multiple choices answer 4", image="https://picsum.photos/300/200", audio="https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0012_8k.wav", multiple_choices=multiple_choices2)

db.session.add_all([multiple_choices_answer1, multiple_choices_answer2, multiple_choices_answer3, multiple_choices_answer4, multiple_choices_answer5, multiple_choices_answer6, multiple_choices_answer7, multiple_choices_answer8])

arrange_sentences_answer_choices1 = Arrange_Sentences_Answer_Choices_Class(word="kata11", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices2 = Arrange_Sentences_Answer_Choices_Class(word="kata21", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices3 = Arrange_Sentences_Answer_Choices_Class(word="kata31", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices4 = Arrange_Sentences_Answer_Choices_Class(word="kata41", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices5 = Arrange_Sentences_Answer_Choices_Class(word="kata51", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices6 = Arrange_Sentences_Answer_Choices_Class(word="kata12", arrange_sentences=arrange_sentences2)
arrange_sentences_answer_choices7 = Arrange_Sentences_Answer_Choices_Class(word="kata22", arrange_sentences=arrange_sentences2)
arrange_sentences_answer_choices8 = Arrange_Sentences_Answer_Choices_Class(word="kata32", arrange_sentences=arrange_sentences2)
arrange_sentences_answer_choices9 = Arrange_Sentences_Answer_Choices_Class(word="kata42", arrange_sentences=arrange_sentences2)
arrange_sentences_answer_choices10 = Arrange_Sentences_Answer_Choices_Class(word="kata52", arrange_sentences=arrange_sentences2)

db.session.add_all([arrange_sentences_answer_choices1,arrange_sentences_answer_choices2,arrange_sentences_answer_choices3,arrange_sentences_answer_choices4,arrange_sentences_answer_choices5])
db.session.add_all([arrange_sentences_answer_choices6,arrange_sentences_answer_choices7,arrange_sentences_answer_choices8,arrange_sentences_answer_choices9,arrange_sentences_answer_choices10])

db.session.commit()