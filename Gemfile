source "https://rubygems.org"

# Uncomment to build our site in Travis-CI and force gh-pages compatibility
# in RVM without gh-pages installed, see:
# - https://pages.github.com/versions/
# - https://docs.travis-ci.com/user/languages/ruby/#default-build-script
# - https://github.com/travis-ci/travis-web/blob/master/Gemfile

ruby "2.7.1"
group :development, :test do
  gem "rake", "~> 12"
end

gem "jekyll", "3.9.0"

group :jekyll_plugins do
  gem "jekyll-sitemap", "1.4.0"
  gem "kramdown-parser-gfm", "1.1.0"
end
