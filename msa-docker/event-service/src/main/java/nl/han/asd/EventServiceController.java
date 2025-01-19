package nl.han.asd;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class EventServiceController {
    @Autowired
    EventServiceService eventServiceService;

    @GetMapping("/events")
    public List<EventDTO> getEvents() {
        return eventServiceService.getEvents();
    }

    @PostMapping("/event")
    public EventDTO addEvent(@RequestBody EventDTO eventDTO) {
        return eventServiceService.addEvent(eventDTO);
    }
}
