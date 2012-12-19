class ApplicationController < ActionController::Base
  protect_from_forgery
  before_filter:begin_request

  def begin_request
	  File.open("/src/temp.txt", "a") { |f|
      	f.puts("A page was loaded at " + Time.now.inspect)
      }
  end

end
