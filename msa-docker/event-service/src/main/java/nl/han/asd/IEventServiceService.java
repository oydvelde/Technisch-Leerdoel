package nl.han.asd;

import java.util.List;

public interface IEventServiceService {
    List<EventDTO> getEvents();

    EventDTO addEvent(EventDTO eventDTO);
}
