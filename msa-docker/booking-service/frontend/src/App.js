import React, {useState, useEffect} from 'react';

const App = () => {
    const [events, setEvents] = useState([]);
    const [bookings, setBookings] = useState({});

    const fetchEvents = () => fetch('http://localhost:6060/events')
        .then(response => response.json())
        .then(data => setEvents(data))  // Zet de evenementen in de state
        .catch(error => console.error('Error fetching events:', error));

    const fetchBookings = () => fetch('http://localhost:6060/bookings')
        .then(response => response.json())
        .then(data => {
            setBookings(data.reduce((acc, booking) => {
                if (acc[booking.event]) {
                    acc[booking.event] += 1;
                } else {
                    acc[booking.event] = 1;
                }
                return acc;
            }, {}));
        })
        .catch(error => console.error('Error fetching bookings:', error));

    useEffect(() => {
        fetchEvents();
        fetchBookings();
    }, []);

    const addBooking = async (eventName) => {
        await fetch('http://localhost:6060/booking', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({event: eventName})  // Stuur het geselecteerde evenement naar de backend
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    setBookings(prevBookings => {
                        const updatedBookings = {...prevBookings};
                        updatedBookings[eventName] = (updatedBookings[eventName] || 0) + 1;
                        return updatedBookings;
                    });
                } else {
                    console.error('Failed to add booking');
                }
            })
            .catch(error => console.error('Error adding booking:', error));
        fetchEvents();
        fetchBookings();
    };

    return (
        <div>
            <h1>Events</h1>
            <ul>
                {events.map(event => (
                    <li key={event.eventId}>
                        {event.eventName}
                        <button onClick={() => addBooking(event.eventName)}>Add Booking</button>
                    </li>
                ))}
            </ul>

            <h2>Bookings</h2>
            <ul>
                {Object.entries(bookings).map(([event, count]) => (
                    <li key={event}>
                        {event}: {count} bookings
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;
