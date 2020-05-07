db.createUser(
    {
        user: "admin",
        pwd: "hadi",
        roles: [
            {
                role: "readWrite",
                db: "db-name"
            }
        ]
    }
);