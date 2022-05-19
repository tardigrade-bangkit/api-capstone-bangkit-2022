from flaskr.model import db,Users,Avatars,Children
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

children1 = Children(name="children1", id_avatar=1, level=1, user=user1, avatar_children=avatar1)
children2 = Children(name="children1", id_avatar=2, level=2, user=user2, avatar_children=avatar2)
children3 = Children(name="children1", id_avatar=3, level=3, user=user3, avatar_children=avatar3)
children4 = Children(name="children1", id_avatar=1, level=4, user=user4, avatar_children=avatar1)
children5 = Children(name="children1", id_avatar=2, level=5, user=user5, avatar_children=avatar2)
children6 = Children(name="children1", id_avatar=3, level=6, user=user6, avatar_children=avatar3)
children7 = Children(name="children1", id_avatar=1, level=7, user=user1, avatar_children=avatar1)
children8 = Children(name="children1", id_avatar=2, level=8, user=user2, avatar_children=avatar2)
children9 = Children(name="children1", id_avatar=3, level=9, user=user3, avatar_children=avatar3)

db.session.add_all([children1,children2,children3,children4,children5,children6,children7,children8,children9])

children1 = Children
children2 = Children
children3 = Children




userA.avatar 
userA.avatar.id 
userA.avatar.image_url


