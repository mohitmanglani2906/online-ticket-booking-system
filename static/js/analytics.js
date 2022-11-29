import {
    TableauViz,
     TableauEventType,
} from 'https://public.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js';

const viz = new TableauViz();
viz.src = 'https://public.tableau.com/views/OnlineTicketBookingRequest/Online_Booking_Request?:language=en-US&:display_count=n&:origin=viz_share_link'
viz.toolbar = 'hidden';
viz.width="1200"
viz.height="800"
document.getElementById('tableauViz').appendChild(viz);