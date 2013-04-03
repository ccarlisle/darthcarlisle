module ApplicationHelper

  def WriteToLogFile(logPrefix, message)

    File.open("/websiteLogs/" + logPrefix + ".txt", "a") { |f|
      f.puts("---------- Message Start --------")

      f.puts(message)

      f.puts("Timestamp: " + Time.now.inspect)

      f.puts("Controller: " + params[:controller])

      f.puts("Action: " + params[:action_name])

      #f.puts("A page was loaded at " + Time.now.inspect+ " by this controller: " + params[:controller] )
    }


  end

end
