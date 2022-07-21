user_cart = """
CREATE TABLE user_cart(
    user_id INT NOT NULL,
    product_id INT NOT NULL);
    
INSERT INTO user_cart VALUES(1,1);
INSERT INTO user_cart VALUES(1,2);
INSERT INTO user_cart VALUES(1,3);
INSERT INTO user_cart VALUES(2,1);
INSERT INTO user_cart VALUES(2,2);
INSERT INTO user_cart VALUES(2,5);

"""

user_favorite = """
CREATE TABLE user_favorite
(
    user_id INT NOT NULL,
    product_id INT NOT NULL
);

INSERT INTO user_favorite VALUES(1,1);
INSERT INTO user_favorite VALUES(1,2);
INSERT INTO user_favorite VALUES(1,3);
INSERT INTO user_favorite VALUES(3,1);
INSERT INTO user_favorite VALUES(3,2);
INSERT INTO user_favorite VALUES(3,3);
    
"""