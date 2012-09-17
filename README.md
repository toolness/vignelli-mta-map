This is just a static, offline-capable version of Massimo Vignelli's 
[diagrammatic map][] of the New York City subway, commissioned by the MTA
in 2011.

To make it, I simply looked at the network log of the [MTA Weekender][]
page to discover that the map is simply a series of tiled 256x256 PNG files.
Then I made a Python script to fetch them all, and recombined them in a
Web page with an appcache manifest.

  [diagrammatic map]: http://tmagazine.blogs.nytimes.com/2011/09/16/ahead-of-its-time-an-icon-goes-digital/
  [MTA Weekender]: http://www.mta.info/weekender.html
