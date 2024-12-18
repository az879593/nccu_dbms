DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE replies (
    reply_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    from_id INTEGER NOT NULL,
    to_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    reply_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
    /* 
    FOREIGN KEY (from_id) REFERENCES users(id), 
    FOREIGN KEY (to_id) REFERENCES users(id)    
    FOREIGN KEY (post_id) REFERENCES posts(id)  
    */  
);