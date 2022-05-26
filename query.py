from flaskr.model import db,Achievements,Lessons_Content,Users,Usages,Avatars,Children,Badges,Lessons,Missions
from flaskr.model import Multiple_choices,Short_answers,Arrange_sentences,Materials,Quizzes,Questions_Class
from flaskr.model import Children_Achievements_Association, Children_Badges_Association, Progress_Association
from flaskr.model import Material_Content_Class, Multiple_Choices_Answers_Class, Arrange_Sentences_Answer_Choices_Class
db.drop_all()
db.create_all()
# Multiple_choices_answers, Arrange_sentences_answer_choices

avatar1 = Avatars(image_url="https://user1wioeurouweruowe.com") 
avatar2 = Avatars(image_url="https://user2wioeurouweruowe.com") 
avatar3 = Avatars(image_url="https://user3wioeurouweruowe.com") 

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

db.session.add_all([children1,children2,children3,children4,children5,children6,children7,children8,children9])

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

badges1 = Badges(image_url="badgesimagesurl1.com")
badges2 = Badges(image_url="badgesimagesurl2.com")
badges3 = Badges(image_url="badgesimagesurl3.com")
badges4 = Badges(image_url="badgesimagesurl4.com")
badges5 = Badges(image_url="badgesimagesurl5.com")
badges6 = Badges(image_url="badgesimagesurl6.com")

db.session.add_all([badges1, badges2, badges3, badges4, badges5, badges6])


# children_badges1 = Children_Badges_Association(acquired_date=20052022, children=1, Badges_id=1)

achievements1 = Achievements(level=1, description="Ini adalah achievement pertamamu")
achievements2 = Achievements(level=2, description="Ini adalah achievement keduamu")
achievements3 = Achievements(level=3, description="Ini adalah achievement ketigamu")

db.session.add_all([achievements1, achievements2, achievements3])

lessons1 = Lessons(cover_image="https://cover_image1", level=1, title="Pelajaran 1", type="Reading", badges=badges1)
lessons2 = Lessons(cover_image="https://cover_image2", level=2, title="Pelajaran 2", type="Writing", badges=badges2)
lessons3 = Lessons(cover_image="https://cover_image3", level=3, title="Pelajaran 3", type="Speaking", badges=badges3)
lessons4 = Lessons(cover_image="https://cover_image4", level=4, title="Pelajaran 4", type="Reading", badges=badges4)
lessons5 = Lessons(cover_image="https://cover_image5", level=5, title="Pelajaran 5", type="Writing", badges=badges5)
lessons6 = Lessons(cover_image="https://cover_image6", level=6, title="Pelajaran 6", type="Speaking", badges=badges6)

db.session.add_all([lessons1, lessons2, lessons3, lessons4, lessons5, lessons6])

missions1 = Missions(title="Ini adalah mission 1", type=1, c_duration=10, c_min_score=10, lessons=lessons1)
missions2 = Missions(title="Ini adalah mission 2", type=2, c_duration=20, c_min_score=20, lessons=lessons2)
missions3 = Missions(title="Ini adalah mission 3", type=3, c_duration=30, c_min_score=30, lessons=lessons1)
missions4 = Missions(title="Ini adalah mission 4", type=4, c_duration=40, c_min_score=40, lessons=lessons2)
missions5 = Missions(title="Ini adalah mission 5", type=5, c_duration=50, c_min_score=50, lessons=lessons3)
missions6 = Missions(title="Ini adalah mission 6", type=6, c_duration=10, c_min_score=10, lessons=lessons4)
missions7 = Missions(title="Ini adalah mission 7", type=7, c_duration=20, c_min_score=20, lessons=lessons3)
missions8 = Missions(title="Ini adalah mission 8", type=8, c_duration=30, c_min_score=30, lessons=lessons5)
missions9 = Missions(title="Ini adalah mission 9", type=9, c_duration=40, c_min_score=40, lessons=lessons6)
missions10 = Missions(title="Ini adalah mission 10", type="Adventures", c_duration=50, c_min_score=50, lessons=lessons5)

db.session.add_all([missions1, missions2, missions3, missions4, missions5, missions6, missions7, missions8, missions9, missions10])


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

multiple_choices1 = Multiple_choices(q_text="What is Yol?", q_image="https://images1.com", q_audio="https://audio1.com", answer="A")
multiple_choices2 = Multiple_choices(q_text="What is Han?", q_image="https://images2.com", q_audio="https://audio2.com", answer="B")
multiple_choices3 = Multiple_choices(q_text="What is Uf?", q_image="https://images3.com", q_audio="https://audio3.com", answer="C")
multiple_choices4 = Multiple_choices(q_text="What is Dan?", q_image="https://images4.com", q_audio="https://audio4.com", answer="D")
multiple_choices5 = Multiple_choices(q_text="What is Tam?", q_image="https://images5.com", q_audio="https://audio5.com", answer="A")
multiple_choices6 = Multiple_choices(q_text="What is Yol?", q_image="https://images1.com", q_audio="https://audio1.com", answer="A")
multiple_choices7 = Multiple_choices(q_text="What is Han?", q_image="https://images2.com", q_audio="https://audio2.com", answer="B")
multiple_choices8 = Multiple_choices(q_text="What is Uf?", q_image="https://images3.com", q_audio="https://audio3.com", answer="C")
multiple_choices9 = Multiple_choices(q_text="What is Dan?", q_image="https://images4.com", q_audio="https://audio4.com", answer="D")
multiple_choices10 = Multiple_choices(q_text="What is Tam?", q_image="https://images5.com", q_audio="https://audio5.com", answer="A")

db.session.add_all([multiple_choices1, multiple_choices2, multiple_choices3, multiple_choices4, multiple_choices5, multiple_choices6, multiple_choices7, multiple_choices8, multiple_choices9, multiple_choices10])

arrange_sentences1 = Arrange_sentences(q_text="What is Yol?", q_image="https://images1.com", q_audio="https://audio1.com", answer="A")
arrange_sentences2 = Arrange_sentences(q_text="What is Han?", q_image="https://images2.com", q_audio="https://audio2.com", answer="B")
arrange_sentences3 = Arrange_sentences(q_text="What is Uf?", q_image="https://images3.com", q_audio="https://audio3.com", answer="C")
arrange_sentences4 = Arrange_sentences(q_text="What is Dan?", q_image="https://images4.com", q_audio="https://audio4.com", answer="D")
arrange_sentences5 = Arrange_sentences(q_text="What is Tam?", q_image="https://images5.com", q_audio="https://audio5.com", answer="A")
arrange_sentences6 = Arrange_sentences(q_text="What is Yol?", q_image="https://images1.com", q_audio="https://audio1.com", answer="A")
arrange_sentences7 = Arrange_sentences(q_text="What is Han?", q_image="https://images2.com", q_audio="https://audio2.com", answer="B")
arrange_sentences8 = Arrange_sentences(q_text="What is Uf?", q_image="https://images3.com", q_audio="https://audio3.com", answer="C")
arrange_sentences9 = Arrange_sentences(q_text="What is Dan?", q_image="https://images4.com", q_audio="https://audio4.com", answer="D")
arrange_sentences10 = Arrange_sentences(q_text="What is Tam?", q_image="https://images5.com", q_audio="https://audio5.com", answer="A")

db.session.add_all([arrange_sentences1, arrange_sentences2, arrange_sentences3, arrange_sentences4, arrange_sentences5, arrange_sentences6, arrange_sentences7, arrange_sentences8, arrange_sentences9, arrange_sentences10])

short_answer1 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Yol?", q_image="https://images1.com", q_audio="https://audio1.com", answer="A")
short_answer2 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Han?", q_image="https://images2.com", q_audio="https://audio2.com", answer="B")
short_answer3 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Uf?", q_image="https://images3.com", q_audio="https://audio3.com", answer="C")
short_answer4 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Dan?", q_image="https://images4.com", q_audio="https://audio4.com", answer="D")
short_answer5 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Tam?", q_image="https://images5.com", q_audio="https://audio5.com", answer="A")
short_answer6 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Yol?", q_image="https://images1.com", q_audio="https://audio1.com", answer="A")
short_answer7 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Han?", q_image="https://images2.com", q_audio="https://audio2.com", answer="B")
short_answer8 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Uf?", q_image="https://images3.com", q_audio="https://audio3.com", answer="C")
short_answer9 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Dan?", q_image="https://images4.com", q_audio="https://audio4.com", answer="D")
short_answer10 = Short_answers(type="ini adalah perubahan dari is_camera", q_text="What is Tam?", q_image="https://images5.com", q_audio="https://audio5.com", answer="A")

db.session.add_all([short_answer1, short_answer2, short_answer3, short_answer4, short_answer5, short_answer6, short_answer7, short_answer8, short_answer9, short_answer10])


quizzes1 = Quizzes()
quizzes2 = Quizzes()
quizzes3 = Quizzes()
quizzes4 = Quizzes()
quizzes5 = Quizzes()
quizzes6 = Quizzes()
quizzes7 = Quizzes()
quizzes8 = Quizzes()
quizzes9 = Quizzes()
quizzes10 = Quizzes()

db.session.add_all([quizzes1, quizzes2, quizzes3, quizzes4, quizzes5, quizzes6, quizzes7, quizzes8, quizzes9, quizzes10])

lessons_content1 = Lessons_Content(order=1, type=1, title="Content belajar pertama", lessons=lessons1, materials=materials1, quizzes=quizzes1)
lessons_content2 = Lessons_Content(order=2, type=2, title="Content belajar kedua", lessons=lessons2, materials=materials2, quizzes=quizzes2)
lessons_content3 = Lessons_Content(order=3, type=3, title="Content belajar ketiga", lessons=lessons3, materials=materials3, quizzes=quizzes3)
lessons_content4 = Lessons_Content(order=4, type=4, title="Content belajar keempat", lessons=lessons4, materials=materials4, quizzes=quizzes4)
lessons_content5 = Lessons_Content(order=5, type=5, title="Content belajar kelima", lessons=lessons5, materials=materials5, quizzes=quizzes5)
lessons_content6 = Lessons_Content(order=1, type=1, title="Content belajar pertama", lessons=lessons1, materials=materials6, quizzes=quizzes6)
lessons_content7 = Lessons_Content(order=2, type=2, title="Content belajar kedua", lessons=lessons2, materials=materials7, quizzes=quizzes7)
lessons_content8 = Lessons_Content(order=3, type=3, title="Content belajar ketiga", lessons=lessons3, materials=materials8, quizzes=quizzes8)
lessons_content9 = Lessons_Content(order=4, type=4, title="Content belajar keempat", lessons=lessons4, materials=materials9, quizzes=quizzes9)
lessons_content10 = Lessons_Content(order=5, type=5, title="Content belajar kelima", lessons=lessons5, materials=materials10, quizzes=quizzes10)

db.session.add_all([lessons_content1, lessons_content2, lessons_content3, lessons_content4, lessons_content5, lessons_content6, lessons_content7, lessons_content8, lessons_content9, lessons_content10])

material_content1 = Material_Content_Class(order=1, text="ini adalah material content 1", image="https://image1.com", audio="https://audio1.com", materials=materials1)
material_content2 = Material_Content_Class(order=2, text="ini adalah material content 2", image="https://image2.com", audio="https://audio2.com", materials=materials2)
material_content3 = Material_Content_Class(order=3, text="ini adalah material content 3", image="https://image3.com", audio="https://audio3.com", materials=materials3)

db.session.add_all([material_content1, material_content2, material_content3])

questions1 = Questions_Class(order=1 , quizzes=quizzes1, multiple_choices=multiple_choices1, arrange_sentences=arrange_sentences1, short_answers=short_answer1)
questions2 = Questions_Class(order=2 , quizzes=quizzes2, multiple_choices=multiple_choices2, arrange_sentences=arrange_sentences2, short_answers=short_answer2)
questions3 = Questions_Class(order=3 , quizzes=quizzes3, multiple_choices=multiple_choices3, arrange_sentences=arrange_sentences3, short_answers=short_answer3)
questions4 = Questions_Class(order=4 , quizzes=quizzes4, multiple_choices=multiple_choices4, arrange_sentences=arrange_sentences4, short_answers=short_answer4)
questions5 = Questions_Class(order=5 , quizzes=quizzes5, multiple_choices=multiple_choices5, arrange_sentences=arrange_sentences5, short_answers=short_answer5)
questions6 = Questions_Class(order=6 , quizzes=quizzes6, multiple_choices=multiple_choices6, arrange_sentences=arrange_sentences6, short_answers=short_answer6)
questions7 = Questions_Class(order=7 , quizzes=quizzes7, multiple_choices=multiple_choices7, arrange_sentences=arrange_sentences7, short_answers=short_answer7)
questions8 = Questions_Class(order=8 , quizzes=quizzes8, multiple_choices=multiple_choices8, arrange_sentences=arrange_sentences8, short_answers=short_answer8)
questions9 = Questions_Class(order=9 , quizzes=quizzes9, multiple_choices=multiple_choices9, arrange_sentences=arrange_sentences9, short_answers=short_answer9)
questions10 = Questions_Class(order=10, quizzes=quizzes10, multiple_choices=multiple_choices10, arrange_sentences=arrange_sentences10, short_answers=short_answer10)

db.session.add_all([questions1, questions2, questions3, questions4, questions5, questions6, questions7, questions8, questions9, questions10])


multiple_choices_answer1 = Multiple_Choices_Answers_Class(choice="A", text="ini adalah multiple choices answer 1", image="https://image1.com", audio="https://audio1.com", multiple_choices=multiple_choices1)
multiple_choices_answer2 = Multiple_Choices_Answers_Class(choice="A", text="ini adalah multiple choices answer 2", image="https://image2.com", audio="https://audio2.com", multiple_choices=multiple_choices2)
multiple_choices_answer3 = Multiple_Choices_Answers_Class(choice="A", text="ini adalah multiple choices answer 3", image="https://image3.com", audio="https://audio3.com", multiple_choices=multiple_choices3)
multiple_choices_answer4 = Multiple_Choices_Answers_Class(choice="A", text="ini adalah multiple choices answer 4", image="https://image4.com", audio="https://audio4.com", multiple_choices=multiple_choices4)
multiple_choices_answer5 = Multiple_Choices_Answers_Class(choice="A", text="ini adalah multiple choices answer 5", image="https://image5.com", audio="https://audio5.com", multiple_choices=multiple_choices5)

db.session.add_all([multiple_choices_answer1, multiple_choices_answer2, multiple_choices_answer3, multiple_choices_answer4, multiple_choices_answer5])

arrange_sentences_answer_choices1 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 1", arrange_sentences=arrange_sentences1)
arrange_sentences_answer_choices2 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 2", arrange_sentences=arrange_sentences2)
arrange_sentences_answer_choices3 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 3", arrange_sentences=arrange_sentences3)
arrange_sentences_answer_choices4 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 4", arrange_sentences=arrange_sentences4)
arrange_sentences_answer_choices5 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 5", arrange_sentences=arrange_sentences5)
arrange_sentences_answer_choices6 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 1", arrange_sentences=arrange_sentences6)
arrange_sentences_answer_choices7 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 2", arrange_sentences=arrange_sentences7)
arrange_sentences_answer_choices8 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 3", arrange_sentences=arrange_sentences8)
arrange_sentences_answer_choices9 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 4", arrange_sentences=arrange_sentences9)
arrange_sentences_answer_choices10 = Arrange_Sentences_Answer_Choices_Class(word="jawaban short answer 5", arrange_sentences=arrange_sentences10)

db.session.add_all([arrange_sentences_answer_choices1,arrange_sentences_answer_choices2,arrange_sentences_answer_choices3,arrange_sentences_answer_choices4,arrange_sentences_answer_choices5])
db.session.add_all([arrange_sentences_answer_choices6,arrange_sentences_answer_choices7,arrange_sentences_answer_choices8,arrange_sentences_answer_choices9,arrange_sentences_answer_choices10])

db.session.commit()