# _data/cv/*.yml is authored to serve two consumers: the LaTeX CV and this
# site. Its values may carry LaTeX markup (\textbf{...}, ---, \%, $\cdot$).
# This filter renders those fragments as HTML so the website can use the same
# strings verbatim, keeping one source of truth.
#
# Custom plugins do not run on the classic GitHub Pages builder, but this site
# builds via GitHub Actions (jekyll-scholar needs that anyway), so it is fine.
module Jekyll
  module TexCleanFilter
    ESCAPES = {
      '\\%'  => '%',
      '\\&'  => '&amp;',
      '\\_'  => '_',
      '\\#'  => '#',
      '\\$'  => '$',
    }.freeze

    def texclean(input)
      return '' if input.nil?
      s = input.to_s.dup

      # inline formatting -> HTML
      s.gsub!(/\\textbf\{([^{}]*)\}/) { "<strong>#{Regexp.last_match(1)}</strong>" }
      s.gsub!(/\\textit\{([^{}]*)\}/) { "<em>#{Regexp.last_match(1)}</em>" }
      s.gsub!(/\\emph\{([^{}]*)\}/)   { "<em>#{Regexp.last_match(1)}</em>" }

      # symbols
      s.gsub!('$\\cdot$', '·')
      s.gsub!('\\cdot', '·')
      s.gsub!('\\\\', ' ')

      # dashes: em before en, or --- turns into two passes
      s.gsub!('---', '—')
      s.gsub!('--', '–')

      ESCAPES.each { |tex, html| s.gsub!(tex, html) }

      # any stray command we do not translate: drop the control sequence
      s.gsub!(/\\[a-zA-Z]+\s*/, '')

      s.squeeze(' ').strip
    end

    # Plain-text variant for attributes and meta tags.
    def texstrip(input)
      texclean(input).gsub(/<[^>]+>/, '')
    end

    # Short label for a domain card: the CV writes a bullet as
    # "NIH SABER---reproducible cloud pipelines"; the card wants "NIH SABER".
    # Entries with no em-dash keep their whole sentence, minus its full stop.
    def card_subject(input)
      s = texstrip(input)
      s = s.split('—').first.to_s.strip
      s.sub(/\.\z/, '')
    end
  end
end

Liquid::Template.register_filter(Jekyll::TexCleanFilter)
