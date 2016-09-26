'use strict';
// //////////////////////////////
		// Setup//
// //////////////////////////////

// Plugins
let gulp = require('gulp'),
  pjson = require('./package.json'),
  gutil = require('gulp-util'),
  sass = require('gulp-sass'),
  autoprefixer = require('gulp-autoprefixer'),
  cssnano = require('gulp-cssnano'),
  rename = require('gulp-rename'),
  del = require('del'),
  plumber = require('gulp-plumber'),
  pixrem = require('gulp-pixrem'),
  uglify = require('gulp-uglify'),
  imagemin = require('gulp-imagemin'),
  exec = require('gulp-exec'),
  runSequence = require('run-sequence'),
  browserSync = require('browser-sync');


// Relative paths function
class pathsConfig {
  constructor(appName) {
    this.app = 'assets/static';
    this.actual_templates = "templates";
    Object.assign(this, {
      app: this.app,
      templates: this.actual_templates + '',
      css: this.app + '/css',
      sass: this.app + '/sass',
      fonts: this.app + '/fonts',
      images: this.app + '/images',
      js: this.app + '/js',
    });
  }
}

let paths = new pathsConfig();
console.log(paths)
// //////////////////////////////
		// Tasks//
// //////////////////////////////

// Styles autoprefixing and minification
gulp.task('styles', function() {
  return gulp.src(paths.sass + '/all.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(plumber()) // Checks for errors
    .pipe(autoprefixer({browsers: ['last 2 version']})) // Adds vendor prefixes
    .pipe(pixrem())  // add fallbacks for rem units
    .pipe(gulp.dest(paths.css))
    .pipe(rename({suffix: '.min'}))
    .pipe(cssnano()) // Minifies the result
    .pipe(gulp.dest(paths.css));
});

// Javascript minification
gulp.task('scripts', function() {
  return gulp.src(paths.js + '/main.js')
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest(paths.js));
});

// Image compression
gulp.task('imgCompression', function() {
  return gulp.src(paths.images + '/*')
    .pipe(imagemin()) // Compresses PNG, JPEG, GIF and SVG images
    .pipe(gulp.dest(paths.images));
});

// Browser sync server for live reload
gulp.task('browserSync', function() {
  browserSync.init(
      [paths.css + '/*.css', paths.js + '*.js', paths.templates + '/*.html'], {
        proxy: '127.0.0.1:5000',
      });
});
gulp.task('templates', function(){
  return gulp.src(paths.templates + '/**/*.html')
    .pipe(browserSync.reload({stream: true}));
});
gulp.task('css', function(){
  return gulp.src(paths.css + '/**/*.css')
    .pipe(browserSync.reload({stream: true}));
});

// Default task
gulp.task('default', function() {
  runSequence(['styles', 
//   'scripts', 
  'imgCompression'], 
//   'runServer', 
  'browserSync');
});

// //////////////////////////////
		// Watch//
// //////////////////////////////

// Watch
gulp.task('watch', ['default'], function() {

  gulp.watch(paths.sass + '/*.scss', ['styles']);
  gulp.watch(paths.css + '/**/*.css', ['css']);
//   gulp.watch(paths.js + '/*.js', ['scripts']);
  gulp.watch(paths.images + '/*', ['imgCompression']);
  gulp.watch(paths.templates + '/**/*.html', ['templates']);

});
