```mermaid
classDiagram
    class User {
        +String firstName
        +String lastName
        +String email
        +String password
        +Boolean isAdmin
        +register()
        +updateProfile()
        +delete()
    }
    class Place {
        +String title
        +String description
        +Float price
        +Float latitude
        +Float longitude
        +create()
        +update()
        +delete()
        +list()
    }
    class Review {
        +Int rating
        +String comment
        +create()
        +update()
        +delete()
        +listByPlace()
    }
    class Amenity {
        +String name
        +String description
        +create()
        +update()
        +delete()
        +list()
    }
    User "1" -- "*" Place : owns
    User "1" -- "*" Review : writes
    Place "1" -- "*" Review : receives
    Place "*" -- "*" Amenity : has