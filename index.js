import * as d3 from "d3";

async function fetchML() {
  let response = await fetch("/predict");
  let data = await response.json();
  return data;
}

document.addEventListener("DOMContentLoaded", () => {
  const hoodDropdown = d3.select("#neighborhood");
  const roomsDropdown = d3.select("#rooms");
  const bathroomsDropdown = d3.select("#bathrooms");
  const neighborhoods = [
    "Bensonhurst",
    "Williamsbridge",
    "Morningside Heights",
    "Tribeca",
    "Port Richmond",
    "Upper West Side",
    "Marble Hill",
    "Glendale",
    "Fordham",
    "New Dorp Beach",
    "Hudson Yards",
    "Midtown East",
    "Mount Hope",
    "Upper East Side",
    "Corona",
    "Tudor City",
    "East Williamsburg",
    "Bushwick",
    "Mott Haven",
    "Woodhaven",
    "Gerritsen Beach",
    "Bayside",
    "Tottenville",
    "Vinegar Hill",
    "Bergen Beach",
    "City Island",
    "Manor Heights",
    "Flatlands",
    "Cypress Hills",
    "Georgetown",
    "Woodside",
    "Gravesend",
    "Laurelton",
    "Maspeth",
    "Chelsea",
    "Financial District",
    "East Flatbush",
    "Sheepshead Bay",
    "Inwood",
    "Kensington",
    "Dyker Heights",
    "Pelham Bay",
    "Carroll Gardens",
    "Melrose",
    "Parkchester",
    "South Williamsburg",
    "WestchesterSquare",
    "Bedford-Stuyvesant",
    "Prospect Heights",
    "Coney Island",
    "Norwood",
    "Sunset Park",
    "East Harlem",
    "Jamaica Estates",
    "Ocean Hill",
    "East Village",
    "Murray Hill",
    "Morrisania",
    "Soho",
    "NoMad",
    "Windsor Terrace",
    "Brighton Beach",
    "Little Italy",
    "Borough Park",
    "Meatpacking",
    "Union Square",
    "Sunnyside",
    "Nolita",
    "Gramercy",
    "Chinatown",
    "Kingsbridge",
    "Ditmas Park",
    "Greenwich Village",
    "Flatbush",
    "Canarsie",
    "Riverdale",
    "Lefferts",
    "Morris Heights",
    "Noho",
    "Forest Hills",
    "Cobble Hill",
    "Jamaica",
    "Greenwood Heights",
    "Concourse Village",
    "Howard Beach",
    "Williamsburg",
    "Kips Bay",
    "Fort Greene",
    "Hudson Heights",
    "Midwood",
    "Oakwood",
    "Hollis",
    "Lower East Side",
    "Roosevelt Island",
    "Throgs Neck",
    "Port Morris",
    "College Point",
    "Clinton Hill",
    "Bedford Park",
    "Gowanus",
    "Soundview",
    "Kew Gardens",
    "Rockaway Beach",
    "DUMBO",
    "Midtown West",
    "Flatiron",
    "East New York",
    "Marine Park",
    "Brownsville",
    "Columbia Street Waterfront",
    "Elmhurst",
    "Astoria",
    "Hunts Point",
    "Battery Park City",
    "Downtown Brooklyn",
    "Harlem",
    "Morris Park",
    "Schuylerville",
    "Boerum Hill",
    "Midtown",
    "Allerton",
    "Stuyvesant Town",
    "LongIsland City",
    "Bay Ridge",
    "Mill Basin",
    "Greenpoint",
    "Rego Park",
    "Richmond Hill",
    "Red Hook",
    "Flushing",
    "Woodlawn",
    "Highbridge",
    "Park Slope",
    "Ridgewood",
    "West Village",
    "Tremont",
    "Brooklyn Heights",
    "Jackson Heights",
    "Washington Heights",
    "Crown Heights"
  ];
  const rooms = [
    "Flex 2",
    "1 Bedroom w/ HO",
    "3 Bedroom",
    "1 Bedroom",
    "6+ Bedroom",
    "Jr 1 Bedroom",
    "5 Bedroom",
    "Flex 3",
    "Flex 4",
    "Building",
    "4 Bedroom w/ HO",
    "3 Bedroomw/ HO",
    "Studio",
    "2 Bedroom w/ HO",
    "Loft",
    "Alcove Studio",
    "Jr 4",
    "4 Bedroom",
    "2 Bedroom"
  ];
  const bathrooms = [
    "2 Bathroom",
    "1.5 Bathroom",
    "4 Bathroom",
    "3.5 Bathroom",
    "3 Bathroom",
    "1 Bathroom",
    "4.5 Bathroom",
    "2.5 Bathroom"
  ];

  neighborhoods.map(neighborhood => {
    hoodDropdown
      .append("option")
      .attr("class", "hood-option")
      .html(neighborhood);
  });
  rooms.map(bedroom => {
    roomsDropdown
      .append("option")
      .attr("class", "rooms-option")
      .html(bedroom);
  });
  bathrooms.map(bathroom => {
    bathroomsDropdown
      .append("option")
      .attr("class", "bathrooms-option")
      .html(bathroom);
  });

  d3.select("#apt-listing").on("submit", () => {
    d3.event.preventDefault();
    fetch;
  });
});
