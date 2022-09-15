package com
import twitter4j._

object SearchStreamer {
  def main(args: Array[String]) {
    val twitterStream = new TwitterStreamFactory(Util.config).getInstance
    twitterStream.addListener(Util.simpleStatusListener)
    twitterStream.filter(new FilterQuery().track("Elon"))
    Thread.sleep(4000)
    twitterStream.cleanUp
    twitterStream.shutdown
  }
}

object Util {
  def simpleStatusListener = new StatusListener() {
  def onStatus(status: Status) { println(status.getText) }
  def onDeletionNotice(statusDeletionNotice: StatusDeletionNotice) {}
  def onTrackLimitationNotice(numberOfLimitedStatuses: Int) {}
  def onException(ex: Exception) { ex.printStackTrace }
  def onScrubGeo(arg0: Long, arg1: Long) {}
  def onStallWarning(warning: StallWarning) {}
  }
  val config = new twitter4j.conf.ConfigurationBuilder()
    .setOAuthConsumerKey("fliAamtun7ixqrljDYF6lnJFs")
    .setOAuthConsumerSecret("uFbPlTKFr72hexcRdIYqby2X6WX6x7U6ALsGZYLcVb9Z9MPNXU")
    .setOAuthAccessToken("552531592-TthuhDkkWR9QdlOitRf1RXN2At0nC7ViBTcutGrz")
    .setOAuthAccessTokenSecret("uVBPFpsuo6tk565i1E2BMvpMojFJ6uBO26vzclbLTVYXs")
    .build
}

