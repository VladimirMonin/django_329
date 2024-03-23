-- Исходная таблица SQLite

CREATE TABLE CardTags (
    CardID INTEGER,
    TagID  INTEGER,
    PRIMARY KEY (
        CardID,
        TagID
    ),
    FOREIGN KEY (
        CardID
    )
    REFERENCES Cards (CardID) ON DELETE CASCADE
                              ON UPDATE CASCADE,
    FOREIGN KEY (
        TagID
    )
    REFERENCES Tags (TagID) ON DELETE CASCADE
                            ON UPDATE CASCADE
);

-- Создаем копию, с полями id, CardID, TagID
-- Переносим туда row_id, CardID, TagID

CREATE TABLE CardTagsCopy (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    CardID INTEGER,
    TagID  INTEGER,
    FOREIGN KEY (
        CardID
    )
    REFERENCES Cards (CardID) ON DELETE CASCADE
                              ON UPDATE CASCADE,
    FOREIGN KEY (
        TagID
    )
    REFERENCES Tags (TagID) ON DELETE CASCADE
                            ON UPDATE CASCADE
);

INSERT INTO CardTagsCopy (CardID, TagID)
SELECT CardID, TagID
FROM CardTags;

-- Удаляем старую таблицу и переименовываем новую

DROP TABLE CardTags;

ALTER TABLE CardTagsCopy
RENAME TO CardTags;