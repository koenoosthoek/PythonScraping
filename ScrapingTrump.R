# Scraping Trump Speeches
## source: https://www.rev.com/blog/transcript-category/donald-trump-transcripts


trump_xpath <- '//div[contains(concat( " ", @class, " " ), concat( " ", "fl-post-grid", " " ))]/div/div/a'

# then run the loop:
for (i in 1:length(list_files_path)) {
  html_out <- read_html(list_files_path[i])
  
  trump_links[i] <- html_elements(html_out, xpath = trump_xpath)
}



# get files for just one page:

trump_url <- "https://www.rev.com/blog/transcript-category/donald-trump-transcripts"
trump_xpath <- '//div[contains(concat( " ", @class, " " ), concat( " ", "fl-post-grid", " " ))]/div/div/a'

trump <- read_html(trump_url)
trump_links <- html_elements(trump, xpath = trump_xpath)

trump_links
