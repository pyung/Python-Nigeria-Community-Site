# Python Nigeria community Site

### Gulp & BrowserSync Section
Ensure your have `node >= 4` on your system.
Create a project directory and run the following commands in a terminal:

    git clone https://github.com/pyung/Python-Nigeria-Community-Site.git pncs
    npm install --global gulp-cli # if you haven't installed gulp
    npm install --save-dev gulp	# Run this command in your project directory
    npm install -g browser-sync # if you haven't installed browser-sync
    npm install

Start up a local server 
<p>If you have python on your system</p>
    
    npm run start

Edit this line in the `gulpfile.js` to point to the local server url setup

    gulp.task('browserSync', function() {
    browserSync.init(
        [paths.css + '/*.css', paths.js + '*.js', paths.templates + '/*.html'], {
            proxy: '127.0.0.1: 8002',
        });
    });


And finally

    gulp watch

This setup also supports `sass` in case you prefer writing sass to css just create the `sass` directory 
<p>and everything should work as expected</p>

**To Deploy**

    lektor build --output-path dist
    npm install -g surge
    cd dist/
    surge . pythonnigeria.org


