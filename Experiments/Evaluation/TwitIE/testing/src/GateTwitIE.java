import gate.*;
import gate.creole.SerialAnalyserController;
import gate.gui.MainFrame;
import gate.util.GateException;

import java.io.File;
import java.net.MalformedURLException;
import gate.Corpus;
import gate.CorpusController;
import gate.Gate;
import gate.creole.ExecutionException;
import gate.creole.ResourceInstantiationException;
import gate.persist.PersistenceException;
import gate.util.persistence.PersistenceManager;
import java.io.File;
import java.io.IOException;
import java.net.URL;

public class GateTwitIE {

    private static CorpusController twiteController;

    public static void main(String[] args) throws GateException, IOException {

        Gate.init();

        // load the TwitIE plugin
        File pluginsDir = Gate.getPluginsHome();
        File twitIEDir = new File(pluginsDir, "Twitter");
        Gate.getCreoleRegister().registerDirectories(twitIEDir.toURI().toURL());




//        initTwitIE();
//        setCorpus(createTestCorpus());
//        execute();
    }

    public static void initTwitIE() throws PersistenceException, IOException, ResourceInstantiationException{
        File pluginsHome = Gate.getPluginsHome();
        File twitterPlugin = new File(pluginsHome,"Twitter");
        File twiteGapp = new File(twitterPlugin,"resources/twitie-en.xgapp");
        twiteController = (CorpusController)PersistenceManager.loadObjectFromFile(twiteGapp);
        System.out.println("... TwiteIE loaded");

    }

    public static void setCorpus(Corpus corpus){
        twiteController.setCorpus(corpus);
    }


    public static void execute() throws ExecutionException{
        System.out.println("Running TwiteIE...");
        twiteController.execute();
        System.out.println("...TwieIE complete");
    }

    public static Corpus createTestCorpus()
            throws MalformedURLException, ResourceInstantiationException {

        Document doc1 = Factory.newDocument(new URL("http://www.wish.org/"));
        //add a dummy feature that will be indexed
        doc1.getFeatures().put("author","Make-A-Wish Foundation");
        doc1.setName("Make-A-Wish document");
        //Document doc1 = Factory.newDocument(new URL("file:///c:/temp/test.txt"));

        Document doc2 = Factory.newDocument(new URL("http://www.until.org"));
        //add a dummy feature that will be indexed
        doc2.getFeatures().put("author","Until There's A Cure Foundation");
        doc2.setName("until.org document");

        assert doc1!=null && doc2!=null;

        // create a corpus with the above documents
        Corpus result = Factory.newCorpus("test corpus");
        assert result != null;
        result.add(doc1);
        result.add(doc2);

        return result;
    }
}
