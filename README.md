Event Registration Platform

A lightweight, responsive web application designed to digitize, streamline, and manage campus events, club activities, and student registrations. 

## Tech Stack & Tools

* **HTML5**: Defines structural blueprints and content layouts for all modules.
* **CSS3**: Handles custom typography, visual accents, and tailored color branding.
* **Bootstrap 5**: Provides a responsive 12-column grid and pre-built UI components.
* **VS Code**: Served as the primary Integrated Development Environment (IDE) for coding.
* **Git & GitHub**: Utilized for source code tracking and collaborative version control.

---

## Project Directory Structure


college-event-registration-platform/
│
├── css/
│   └── style.css            # Custom layout overrides and design themes
├── js/
│   └── main.js             # Form validations and modal triggers
├── admin/
│   ├── dashboard.html       # Overview of registrations and stats
│   └── manage-events.html   # Event creation and student tracking form
├── index.html               # Main landing page showcasing ongoing events
├── signup.html              # Role-based student and organizer signup
├── dashboard.html           # Student registration and discovery panel
└── README.md                # Project documentation and guide
```

---

## Core Modules & Workflow

### 1. Signup System
* **User Input**: Captures student names, official college emails, roll numbers, and passwords.
* **Validation**: Restricts entry errors using native form attributes (`required`, `type="email"`).
* **Role Selection**: Implements a choice dropdown to distinguish between standard Student views and Club Organizer permissions.

### 2. Student Dashboard
* **Event Discovery**: Features an organized visual grid of ongoing and upcoming campus events.
* **Category Filters**: Implements sorting tags to navigate between technical workshops, cultural fests, and sports.
* **Registration Action**: Triggers a Bootstrap confirmation modal allowing instant registration with a single click.

### 3. Admin Side
* **Metrics Overview**: Displays interactive numeric metrics for total signups and active live events.
* **Event Creation Form**: Hosts dedicated input modules to upload banners, event descriptions, schedules, and venues.
* **Attendee Management**: Integrates clean layout data tables listing all registered students for event check-ins.

---

## Challenges Faced & Solutions

* **Mobile Table Layouts**: Complex administrative student tables broke horizontally on smaller phone layouts.
  * *Fix*: Applied Bootstrap’s `.table-responsive` wrapper class to enable smooth horizontal scrolling on mobile.
* **CSS Styling Overrides**: Custom design rules in `style.css` inadvertently corrupted structural Bootstrap utilities.
  * *Fix*: Re-arranged the HTML `<head>` tags to ensure the custom stylesheet loads strictly *after* the Bootstrap CDN.
* **Long Form Drop-Offs**: Extended single-page forms led to user confusion during mobile testing.
  * *Fix*: Restructured layouts using grid systems to pack components together cleanly and save vertical screen space.

---

## Testing Phase

* **Cross-Browser Verification**: Confirmed layout rendering uniformity across Google Chrome, Apple Safari, and Mozilla Firefox.
* **Device Emulation**: Leveraged Chrome DevTools to simulate and fine-tune scaling on smartphones, tablets, and desktop displays.
* **Validation Testing**: Verified that submission processes halt and display precise inline alert warnings when fields are missing data.

---

## Conclusion

This Event Management Platform replaces manual paperwork with an organized platform. Utilizing HTML, CSS, and Bootstrap accelerates the user interface layout lifecycle, delivering an optimized utility application built to handle event registrations and helps the admin to manage and monitor platform activity in real-time through a clean, distraction-free environment.
