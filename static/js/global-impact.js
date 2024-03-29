var myearth;
var localNewsMarker;
var news = [];

window.addEventListener( "earthjsload", function() {

	myearth = new Earth( document.getElementById('element'), {

		location : {lat: 18, lng: 50},
		zoom: 1.05,
		light: 'none',

		transparent : true,
		mapSeaColor : 'RGBA(255,255,255,0.76)',
		mapLandColor : '#383838',
		mapBorderColor : '#5D5D5D',
		mapBorderWidth : 0.25,
		mapStyles : ' #CU, #DO, #HT, #JM, #PR ',
		mapHitTest : true,

		autoRotate: true,
		autoRotateSpeed: 0.7,
		autoRotateDelay: 4000,

	} );


	myearth.addEventListener( "ready", function() {

		this.startAutoRotate();


		// Caribbean

		news[0] = myearth.addOverlay( {
			location: {lat: 27.5, lng: -71},
			offset: 0.3,
			depthScale : 0.25,
			className : 'warning',
			occlude: false,

			newsId : 0 // custom property
		} );

		news[0].element.addEventListener( 'click', highlightBreakingNews );


		// Mongolia

		news[1] = myearth.addOverlay( {
			location: {lat: 49, lng: 106},
			offset: 0.3,
			depthScale : 0.25,
			className : 'warning',
			occlude: false,

			newsId : 1
		} );

		news[1].element.addEventListener( 'click', highlightBreakingNews );

		myearth.addLine({
			polyLine : true,
			locations: [
				{lat: 50, lng: 100},
				{lat: 43, lng: 100},
				{lat: 43, lng: 96},
				{lat: 46, lng: 90},
				{lat: 50, lng: 90},
				{lat: 50, lng: 100}
			],
			color : "",
			width: 0.75
		});


		// Sumatra

		news[2] = myearth.addOverlay( {
			location: {lat: 4, lng: 91.5},
			offset: 0.3,
			depthScale : 0.25,
			className : 'warning',
			occlude: false,

			newsId : 2
		} );

		news[2].element.addEventListener( 'click', highlightBreakingNews );

		myearth.addMarker( {
			location: {lat: 3.52, lng: 97.3},
			mesh : "Pin3",
			color : "",
			scale: 0.4,
			hotspot: false,
		} );


	} );



	var selectedCountry;

	myearth.addEventListener( 'click', function( event ) {

		if ( event.id ) {

			if ( selectedCountry != event.id ) {
				selectedCountry = event.id;
				document.getElementById('country-name').innerHTML = countries[ event.id ];
				document.getElementById('local-news').classList.add( 'has-news' );
				document.getElementById('local-news').classList.toggle( 'toggle-news' );
			}

			// create news marker on first click

			if ( ! localNewsMarker ) {

				localNewsMarker = this.addMarker( {
					mesh : "Marker",
					color: '#257cff',
					location : event.location,
					scale: 0.01
				} );

				localNewsMarker.animate( 'scale', 0.9, { easing: 'out-back' } );

			} else {

				localNewsMarker.animate( 'location', event.location, { duration: 200, relativeDuration: 50, easing: 'in-out-cubic' } );

			}

		}

	} );

} );


function highlightBreakingNews( event ) {

	var overlay = event.target.closest('.earth-overlay').overlay;
	var newsId = overlay.newsId;

	document.getElementById( 'breaking-news-'+ newsId ).classList.add( 'news-highlight' );
	setTimeout( function(){
		document.getElementById( 'breaking-news-'+ newsId ).classList.remove( 'news-highlight' );
	}, 500 );

	myearth.goTo( overlay.location, { duration: 250, relativeDuration: 70 } );

	event.stopPropagation();
}

function gotoBreakingNews( newsId ) {

	myearth.goTo( news[ newsId ].location, { duration: 250, relativeDuration: 70 } );

}