INSERT INTO assets (path) VALUES (
    CONCAT(
        "images/avatar",
        FLOOR(rand() * 100000),
        ".png"
    )
);
INSERT INTO assets (path) VALUES (
    CONCAT(
        "avatar/avatar",
        FLOOR(rand() * 100000),
        ".png"
    )
);
