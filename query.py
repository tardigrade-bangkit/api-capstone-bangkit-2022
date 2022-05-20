from flaskr.model import Achievements, db,Users,Avatars,Children,Badges,Children_Badges_Association,Lessons
db.drop_all()
db.create_all()

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

lessons1 = Lessons(cover_image="https://cover_image1", level=1, title="Pelajaran 1", type="Reading", badges=badges1, achievements=achievements1)
lessons2 = Lessons(cover_image="https://cover_image2", level=2, title="Pelajaran 2", type="Writing", badges=badges2, achievements=achievements1)
lessons3 = Lessons(cover_image="https://cover_image3", level=3, title="Pelajaran 3", type="Speaking", badges=badges3, achievements=achievements2)
lessons4 = Lessons(cover_image="https://cover_image4", level=4, title="Pelajaran 4", type="Reading", badges=badges4, achievements=achievements2)
lessons5 = Lessons(cover_image="https://cover_image5", level=5, title="Pelajaran 5", type="Writing", badges=badges5, achievements=achievements3)
lessons6 = Lessons(cover_image="https://cover_image6", level=6, title="Pelajaran 6", type="Speaking", badges=badges6, achievements=achievements3)

db.session.add_all([lessons1, lessons2, lessons3, lessons4, lessons5, lessons6])

db.session.commit()