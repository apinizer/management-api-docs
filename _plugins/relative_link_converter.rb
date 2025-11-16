module Jekyll
  class RelativeLinkConverter < Converter
    safe true
    priority :low

    def matches(ext)
      ext =~ /^\.md$/i
    end

    def output_ext(ext)
      ".html"
    end

    def convert(content)
      # Site baseurl'i al
      baseurl = @config['baseurl'] || ''
      
      # Markdown içindeki absolute path'leri baseurl ile birleştir
      # Pattern: ](/path/to/page) -> ]({{ site.baseurl }}/path/to/page)
      content.gsub!(/\]\((\/[^)]+)\)/) do |match|
        path = $1
        # External link değilse baseurl ekle
        unless path.start_with?('//') || path.start_with?('http')
          if baseurl && !baseurl.empty?
            "](" + baseurl + path + ")"
          else
            match
          end
        else
          match
        end
      end
      
      content
    end
  end
end

