const navbar = `<aside id="fh5co-aside" role="complementary" class="border js-fullheight">
            <nav id="fh5co-main-menu" role="navigation">
                <ul>
                    <li class="fh5co-active"><a href="home">Home</a></li>
                    <!--<li class="fh5co-active"><a href="cancel-ticket">Cancel Ticket</a></li>-->
                    <li class="fh5co-active"><a href="search-ticket-view">Search Ticket</a></li>
                </ul>
            </nav>
        </aside>`;

var initNavBar = () => window.addEventListener('DOMContentLoaded', () => {
              let barnav = document.querySelector('nav[role="navigation"]');
              barnav.innerHTML = navbar;
            });

initNavBar()

