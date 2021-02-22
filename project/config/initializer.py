#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('Database.db')

with con:
    
    cur = con.cursor()
    
    #Create data for the user table
    cur.execute("CREATE TABLE users(UserId INT, UserName TEXT, FullName TEXT, Password TEXT, Picture TEXT, banner TEXT, job TEXT, overview TEXT, exp TEXT, linkedin TEXT)")
    cur.execute("INSERT INTO users VALUES(1,'admin', 'Bala Krishna', 'a85bf7da9f74a3b5185570db78460971', 'stock.gif', 'banner.png', 'Actor', 'Nandamuri Balakrishna, known as Balakrishna, is a dynamic Indian film actor and politician. He appeared in more than 100 Telugu films over forty years in a variety of roles and established himself as one of the leading actors of Telugu cinema. He won three Nandi Awards and one South Indian International Movie Award', 'Actor, Dancer, Singer, Hacker', 'https://www.linkedin.com/in/glenn-ten-cate')")
    cur.execute("INSERT INTO users VALUES(2,'Moderator', 'Tony Stark', '0d107d09f5bbe40cade3de5c71e9e9b7', 'meloncat.jpg', 'banner.png', 'Security Engineer', 'A wealthy American business magnate, playboy, philanthropist, inventor and ingenious scientist, Anthony Edward "Tony" Stark suffers a severe chest injury during a kidnapping.', 'Genius, Billionaire, Playboy, Philanthropist', 'https://www.linkedin.com/in/riccardo-ten-cate-a0b79780')")
    cur.execute("INSERT INTO users VALUES(3,'Test', 'test test', '098f6bcd4621d373cade4e832627b4f6', 'anon.png', 'banner-stock1.jpg', 'Software developer', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque tempor aliquam felis, nec condimentum ipsum commodo id. Vivamus sit amet augue nec urna efficitur tincidunt. Vivamus consectetur aliquam lectus commodo viverra. Nunc eu augue nec arcu efficitur faucibus. Aliquam accumsan ac magna convallis bibendum. Quisque laoreet augue eget augue fermentum scelerisque. Vivamus dignissim mollis est dictum blandit. Nam porta auctor neque sed congue. Nullam rutrum eget ex at maximus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget vestibulum lorem.', 'Software developer, tester', 'https://www.linkedin.com/in/blabla')")
    cur.execute("INSERT INTO users VALUES(4,'John92', 'John Doe', '0cbdc7572ff7d07cc6807a5b102a3b93', 'Aybabtu.png', 'banner-stock2.jpg', 'Chief Information Officer', 'Ipsum dolor sit amet, consectetur adipiscing elit. Quisque tempor aliquam felis, nec condimentum ipsum commodo id. Vivamus sit amet augue nec urna efficitur tincidunt. Vivamus consectetur aliquam lectus commodo viverra. Nunc eu augue nec arcu efficitur faucibus. Aliquam accumsan ac magna convallis bibendum. Quisque laoreet augue eget augue fermentum scelerisque. Vivamus dignissim mollis est dictum blandit', 'Security Policy, Security Controls, Audits', 'https://www.linkedin.com/in/foobar')")

    #Create some data for pageinformation
    cur.execute("CREATE TABLE pages(pageId INT, title TEXT, content TEXT)")
    cur.execute("INSERT INTO pages VALUES(1,'The Dashboard','So, here we are. After a lot of hard work and hassle here we have the dashboard finally up and running. Please take note of this message since it will be updated a lot!')")
    cur.execute("INSERT INTO pages VALUES(2,'Seccond page','Why is there a seccond page, we are going to update the first one right?')")

    con.commit()
    #con.close()
