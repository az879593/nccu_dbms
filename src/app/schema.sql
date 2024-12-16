DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE replies (
    reply_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reply_userid TEXT NOT NULL,
    post_id INTEGER NOT NULL,
    post_userid INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    /* 
    FOREIGN KEY (reply_userid) REFERENCES users(id), 
    FOREIGN KEY (post_userid) REFERENCES users(id),  
    FOREIGN KEY (post_id) REFERENCES posts(id) 
    */     
);