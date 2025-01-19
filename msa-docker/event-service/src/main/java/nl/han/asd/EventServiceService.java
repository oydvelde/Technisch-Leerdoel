package nl.han.asd;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EventServiceService implements IEventServiceService {
    @Autowired
    EventRepository eventRepository;

    @Override
    public List<EventDTO> getEvents() {
        return eventRepository.findAll();
    }

    @Override
    public EventDTO addEvent(EventDTO eventDTO) {
        return eventRepository.save(eventDTO);
    }
}
