source "https://rubygems.org"

# Force gh-pages compatibility in RVM without gh-pages installed
# see https://pages.github.com/versions/
ruby "2.5.3"

# Uncomment to build our site in Travis-CI
# see https://docs.travis-ci.com/user/languages/ruby/#default-build-script
# and https://github.com/travis-ci/travis-web/blob/master/Gemfile
group :development, :test do
  gem "rake", "~> 12"
end

gem "jekyll", "3.8.5"

group :jekyll_plugins do
  gem "jekyll-sitemap", "1.4.0"
end
