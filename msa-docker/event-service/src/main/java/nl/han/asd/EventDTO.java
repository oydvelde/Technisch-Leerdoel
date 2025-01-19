package nl.han.asd;

import jakarta.persistence.*;

@Entity
@Table(name = "Event")
public class EventDTO {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    @Column(name = "eventID")
    private int eventId;

    @Column(name = "eventName")
    private String eventName;

    public int getEventId() {
        return eventId;
    }

    public void setEventId(int eventId) {
        this.eventId = eventId;
    }

    public String getEventName() {
        return eventName;
    }

    public void setEventName(String eventName) {
        this.eventName = eventName;
    }
}
