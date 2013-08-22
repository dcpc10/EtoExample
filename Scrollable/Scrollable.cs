//
// Scrollable.cs
//
// Author:
//       SjB <steve@sagacity.ca>
//
// Copyright (c) 2012 Sagacity Solutions Inc
//

using System;

using Eto.Forms;
using Eto.Drawing;

namespace Sagacity.EtoExample
{
	public class MainAppForm : Form
	{
		const string APP_TITLE = "Scrollable Example";
		static readonly Size DEFAULT_WINDOW_SIZE = new Size(800, 600);

		static void Main(string[] args)
		{
			var app = new Application();
			app.Name = APP_TITLE;

			app.Initialized += delegate {
				app.MainForm = new MainAppForm();
				app.MainForm.Show();
			};
			app.Run(args);
		}

		MainAppForm()
		{
			//Size = DEFAULT_WINDOW_SIZE;
			var blue_panel = new Panel { Size = new Size(200, 200), BackgroundColor = Colors.Blue };
			var green_panel = new Panel { Size = new Size(200, 200), BackgroundColor = Colors.Green };
			var button = new Button { Text = "Toggle" };
			button.Click += delegate {
				blue_panel.Visible = !blue_panel.Visible;
			};

			var scroll_layout = new DynamicLayout(new Scrollable());
			scroll_layout.Add(button);
			scroll_layout.Add(blue_panel);
			scroll_layout.Add(green_panel);

			var form_layout = new DynamicLayout(this);
			form_layout.Add(scroll_layout.Container);
		}
	}
}
